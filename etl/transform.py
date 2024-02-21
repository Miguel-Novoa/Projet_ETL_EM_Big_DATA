import sys
import pandas as pd
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import sqlite3
from xml.dom.minidom import parse


def read_csv(input_file):
    return pd.read_csv(input_file)

def read_json(input_file):
    return pd.read_json(input_file)

def read_xml(input_file):
    return pd.read_xml(input_file)

def read_html(input_file):
    df_list = pd.read_html(input_file)  # Returns a list of DataFrames
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df


def read_sql(input_file):
    conn = sqlite3.connect(input_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic")
    data = cursor.fetchall()
    conn.close()
    return data

def write_json(data, output_file):
    if isinstance(data, pd.DataFrame):  # Check if data is a DataFrame
        # Convert DataFrame to list of dictionaries
        data_dict = data.to_dict(orient='records')
        # Write the converted data to JSON file
        with open(output_file, 'w') as f:
            json.dump(data_dict, f, indent=4)
    else:
        print("Data is not a DataFrame. Cannot write to JSON.")


def write_xml(data, output_file):
    root = ET.Element("data")
    for record in data:
        rec = ET.SubElement(root, "record")
        for key, value in record.items():
            field = ET.SubElement(rec, key)
            field.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True, method="xml", short_empty_elements=False)
    # Lecture du fichier XML pour formater l'indentation
    dom = parse(output_file)
    # Écriture du fichier XML avec une meilleure indentation
    with open(output_file, 'w') as f:
        f.write(dom.toprettyxml(indent="    "))

def write_html(data, output_file):
    with open(output_file, 'w') as f:
        f.write("<html>\n")
        f.write("    <body>\n")
        f.write("        <table>\n")
        for row in data:
            f.write("            <tr>\n")
            for col in row:
                f.write("                <td>{}</td>\n".format(col))
            f.write("            </tr>\n")
        f.write("        </table>\n")
        f.write("    </body>\n")
        f.write("</html>\n")

def write_sql(data, output_file):
    conn = sqlite3.connect(output_file)
    data.to_sql('titanic', conn, index=False, if_exists='replace')
    conn.close()

def write_csv(data, output_file):
    if isinstance(data, pd.DataFrame):  # Check if data is a DataFrame
        data.to_csv(output_file, index=False)
    else:
        # Handle the case where data is not a DataFrame
        # For example, you might want to convert it to a DataFrame first or handle it differently
        print("Data is not a DataFrame. Cannot write to CSV.")



def main():
    if len(sys.argv) < 4:
        print("Usage: python transform.py <input_file> <output_formats> <input_format>")
        return

    input_file = sys.argv[1]
    output_formats = sys.argv[2].split(',')
    input_format = sys.argv[3]

    # Read input data based on input format
    if input_format == 'csv':
        data = read_csv(input_file)
    elif input_format == 'json':
        data = read_json(input_file)
    elif input_format == 'xml':
        data = read_xml(input_file)
    elif input_format == 'html':
        data = read_html(input_file)
    elif input_format == 'sql':
        data = read_sql(input_file)
    else:
        print("Invalid input format")
        return

    # Write output data based on output formats
    for output_format in output_formats:
        output_file = f"../out/titanic_50.{output_format}"

        if isinstance(data, pd.DataFrame):  # Check if data is a DataFrame
            if output_format == 'json':
                data.to_json(output_file, orient='records', indent=4)
            elif output_format == 'csv':
                data.to_csv(output_file, index=False)
            elif output_format == 'xml':
                write_xml(data.to_dict(orient='records'), output_file)  # Convert DataFrame to dictionary before writing XML
            elif output_format == 'html':
                write_html(data.values.tolist(), output_file)
            elif output_format == 'sql':
                write_sql(data, output_file)
        else:
            if output_format == 'json':
                write_json(data, output_file)
            elif output_format == 'xml':
                write_xml(data, output_file)
            elif output_format == 'html':
                write_html(data, output_file)
            elif output_format == 'csv':
                write_csv(data, output_file)
            elif output_format == 'sql':
                write_sql(data, output_file)
            else:
                print("Invalid output format")


if __name__ == "__main__":
    main()
