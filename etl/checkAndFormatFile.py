import pandas as pd
import json
import sys
import os

def check_csv_file(csv_file, expected_encoding='utf-8', expected_separator=','):
    try:
        # Vérification de l'encodage
        with open(csv_file, encoding=expected_encoding) as f:
            f.read()
        print(f"CSV file encoding is correct (expected: {expected_encoding}).")

        # Vérification du séparateur
        df = pd.read_csv(csv_file, sep=expected_separator)
        print(f"CSV file separator is correct (expected: {expected_separator}).")

        # Vérification des données manquantes
        missing_data = df.isnull().sum().sum()
        if missing_data > 0:
            print(f"There are {missing_data} missing values in the CSV file.")
            # Ajouter ici une indication sur les lignes où se trouvent les données manquantes
            print("Rows with missing values:")
            print(df[df.isnull().any(axis=1)])
        else:
            print("No missing values in the CSV file.")

    except UnicodeDecodeError as e:
        print(f"Error decoding CSV file. Encoding may not be {expected_encoding}.")
        print(f"Error details: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
    except pd.errors.EmptyDataError:
        print("Empty CSV file.")

def check_csv_file_and_format_csv(csv_file, expected_encoding='utf-8', expected_separator=','):
    try:
        # Vérification de l'encodage
        with open(csv_file, encoding=expected_encoding) as f:
            f.read()
        print(f"CSV file encoding is correct (expected: {expected_encoding}).")

        # Vérification du séparateur
        df = pd.read_csv(csv_file, sep=expected_separator)
        print(f"CSV file separator is correct (expected: {expected_separator}).")

        # Vérification des données manquantes
        missing_data = df.isnull().sum().sum()
        if missing_data > 0:
            print(f"There are {missing_data} missing values in the CSV file.")
            # Ajouter ici une indication sur les lignes où se trouvent les données manquantes
            print("Rows with missing values:")
            print(df[df.isnull().any(axis=1)])
        else:
            print("No missing values in the CSV file.")

        # Formater l'encodage et le séparateur si nécessaire
        if df.encoding != expected_encoding or df.sep != expected_separator:
            formatted_df = pd.read_csv(csv_file, encoding=expected_encoding, sep=expected_separator)
            # Écrire le fichier formaté dans le dossier ../out
            formatted_file_path = os.path.join('..', 'out', os.path.basename(csv_file).replace('.csv', '_formatted.csv'))
            formatted_df.to_csv(formatted_file_path, index=False)
            print(f"Formatted CSV written to {formatted_file_path}")

    except UnicodeDecodeError as e:
        print(f"Error decoding CSV file. Encoding may not be {expected_encoding}.")
        print(f"Error details: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
    except pd.errors.EmptyDataError:
        print("Empty CSV file.")


def check_missing_data_and_format_json(data):
    # Function to check for missing values and format the data
    def recursive_check_and_format(obj, current_path=[]):
        missing_data_count = 0

        for column in obj.columns:
            current_path.append(column)
            if obj[column].isnull().any() or (obj[column] == "").any():
                print(f"Missing value in column '{'.'.join(current_path)}'")
                column_missing_data = obj[column].isnull().sum() + (obj[column] == "").sum()
                missing_data_count += column_missing_data
                print("Number of missing values:", column_missing_data)
                # Replace empty strings with quotes
                obj[column] = obj[column].fillna('""').replace("", 'null')

            current_path.pop()

        return missing_data_count

    missing_data_count = recursive_check_and_format(data)
    
    if missing_data_count > 0:
        print(f"There are {missing_data_count} missing values in the JSON file.")
        return data
    else:
        print("No missing values in the JSON file.")
        return data