import pandas as pd
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import sqlite3

def readData(inputFile, inputFormat):
    if inputFormat == 'csv':
        return readCsv(inputFile)
    elif inputFormat == 'json':
        return readJson(inputFile)
    elif inputFormat == 'xml':
        return readXml(inputFile)
    elif inputFormat == 'html':
        return readHtml(inputFile)
    elif inputFormat == 'sql':
        return readSql(inputFile)
    else:
        print("Invalid input format")
        return None

def readCsv(inputFile):
    return pd.read_csv(inputFile)

def readJson(inputFile):
    return pd.read_json(inputFile)

def readXml(inputFile):
    return pd.read_xml(inputFile)

def readHtml(inputFile):
    df_list = pd.read_html(inputFile)  # Returns a list of DataFrames
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def readSql(inputFile):
    conn = sqlite3.connect(inputFile)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic")
    data = cursor.fetchall()
    conn.close()
    return data
