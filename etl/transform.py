import csv
import json
import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

def read_csv(input_file_path):
    data = []
    with open(input_file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def write_json(data, output_file_path):
    with open(output_file_path, 'w') as f:
        json.dump(data, f, indent=4)

def write_xml(data, output_file_path):
    root = ET.Element("data")
    for record in data:
        record_element = ET.SubElement(root, "record")
        for key, value in record.items():
            field_element = ET.SubElement(record_element, key)
            field_element.text = str(value)
    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
    with open(output_file_path, 'w') as f:
        f.write(xmlstr)

def write_html(data, output_file_path):
    with open(output_file_path, 'w') as f:
        f.write("<html>\n")
        f.write("<head><title>Titanic Data</title></head>\n")
        f.write("<body>\n")
        f.write("<table border='1'>\n")
        f.write("<tr>\n")
        for key in data[0].keys():
            f.write(f"    <th>{key}</th>\n")
        f.write("</tr>\n")
        for record in data:
            f.write("<tr>\n")
            for value in record.values():
                f.write(f"    <td>{value}</td>\n")
            f.write("</tr>\n")
        f.write("</table>\n")
        f.write("</body>\n")
        f.write("</html>\n")

def main():
    if len(sys.argv) < 4:
        print("Utilisation: python transform.py <fichier_csv> --input-format <format> --output-formats <formats>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_formats = sys.argv[5:]

    input_file_name = os.path.splitext(os.path.basename(input_file_path))[0]

    data = read_csv(input_file_path)

    if not output_formats:
        print("Aucun format de sortie spécifié.")
        sys.exit(1)

    for format in output_formats:
        if format == 'json':
            output_file_path = os.path.join('../out', f"{input_file_name}_{format}.{format}")
            write_json(data, output_file_path)
            print(f"Fichier JSON généré : {output_file_path}")
        elif format == 'xml':
            output_file_path = os.path.join('../out', f"{input_file_name}_{format}.{format}")
            write_xml(data, output_file_path)
            print(f"Fichier XML généré : {output_file_path}")
        elif format == 'html':
            output_file_path = os.path.join('../out', f"{input_file_name}_{format}.{format}")
            write_html(data, output_file_path)
            print(f"Fichier HTML généré : {output_file_path}")
        else:
            print(f"Format de sortie non pris en charge : {format}")

if __name__ == "__main__":
    main()
