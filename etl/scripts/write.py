import pandas as pd
import json
import sqlite3
from lxml import etree

def writeData(outputFile, outputFormats, data):
    baseFileName = outputFile
    
    for outputFormat in outputFormats:
        outputFile = f"{baseFileName}.{outputFormat}"
        if outputFormat == 'csv':
            writeCsv(outputFile, data)
        elif outputFormat == 'json':
            writeJson(outputFile, data)
        elif outputFormat == 'xml':
            writeXml(outputFile, data)
        elif outputFormat == 'html':
            writeHtml(outputFile, data)
        elif outputFormat == 'sql':
            writeSql(outputFile, data)
        elif outputFormat == 'txt':
            writeTxt(outputFile, data)
        else:
            print(f"Invalid output format: {outputFormat}")

def writeJson(outputFile, data):
    if isinstance(data, pd.DataFrame):  # Check if data is a DataFrame
        # Convert DataFrame to list of dictionaries
        data_dict = data.to_dict(orient='records')
        # Write the converted data to JSON file
        with open(outputFile, 'w') as f:
            json.dump(data_dict, f, indent=4)
    else:
        print("Data is not a DataFrame. Cannot write to JSON.")

def writeXml(outputFile, data):
    # Convert DataFrame to dictionary
    data_dict = data.to_dict(orient='records')
    
    # Replace spaces in column names with underscores in dictionary keys
    data_dict = [{col.replace(' ', '_'): val for col, val in record.items()} for record in data_dict]
    
    # Convert dictionary to XML Element
    root = etree.Element("data")
    for record in data_dict:
        rec = etree.SubElement(root, "record")
        for key, value in record.items():
            field = etree.SubElement(rec, key)
            field.text = str(value)
    
    # Write XML content to file with indentation
    with open(outputFile, 'wb') as f:
        f.write(etree.tostring(root, pretty_print=True))

def writeHtml(outputFile, data):
    with open(outputFile, 'w') as f:
        f.write("<html>\n")
        f.write("    <body>\n")
        f.write("        <table>\n")
        
        # Write header row with column names
        f.write("            <tr>\n")
        for col_name in data.columns:
            f.write("                <th>{}</th>\n".format(col_name))
        f.write("            </tr>\n")
        
        # Iterate over each row in the DataFrame
        for _, row in data.iterrows():
            f.write("            <tr>\n")
            
            # Iterate over each value in the row
            for col in row:
                f.write("                <td>{}</td>\n".format(col))
                
            f.write("            </tr>\n")
        
        f.write("        </table>\n")
        f.write("    </body>\n")
        f.write("</html>\n")



def writeSql(outputFile, data):
    conn = sqlite3.connect(outputFile)
    data.to_sql('titanic', conn, index=False, if_exists='replace')
    conn.close()

def writeCsv(outputFile, data):
    # Write DataFrame to CSV file
    data.to_csv(outputFile, index=False)

def writeTxt(outputFile, data):
    data.to_csv(outputFile, sep='\t', index=False)
