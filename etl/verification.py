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

def check_missing_data_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    
    # Fonction pour vérifier la présence de valeurs manquantes
    def is_missing(value):
        return value == "" or pd.isnull(value)

    # Fonction récursive pour parcourir les données JSON
    def recursive_check(obj, current_path=[]):
        missing_data_count = 0
        if isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path.append(i)
                missing_data_count += recursive_check(item, current_path)
                current_path.pop()
        elif isinstance(obj, dict):
            for key, value in obj.items():
                current_path.append(key)
                if is_missing(value):
                    print(f"Missing value at path '{'.'.join(map(str, current_path))}'")
                    missing_data_count += 1
                elif isinstance(value, (list, dict)):
                    missing_data_count += recursive_check(value, current_path)
                current_path.pop()
        return missing_data_count

    missing_data_count = recursive_check(data)
    
    if missing_data_count > 0:
        print(f"There are {missing_data_count} missing values in the JSON file.")
    else:
        print("No missing values in the JSON file.")

def check_missing_data_and_format_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    
    # Fonction pour vérifier la présence de valeurs manquantes et formater les données
    def recursive_check_and_format(obj, current_path=[]):
        missing_data_count = 0

        if isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path.append(str(i))
                missing_data_count += recursive_check_and_format(item, current_path)
                current_path.pop()
        elif isinstance(obj, dict):
            for key, value in obj.items():
                current_path.append(str(key))
                if pd.isnull(value) or value == "":
                    print(f"Missing value in key '{'.'.join(current_path)}' at line {current_path[-1]}")
                    missing_data_count += 1
                    # Ajouter des guillemets à une chaîne vide
                    obj[key] = '""'
                elif isinstance(value, str) and not (value.startswith('"') and value.endswith('"')):
                    # Ajouter des guillemets si la valeur est une chaîne mais n'en possède pas
                    obj[key] = f'"{value}"'
                    # Si la chaîne représente un nombre, convertir
                    obj[key] = convert_to_number(value)
                    # Si la chaîne représente un booléen, convertir
                    if value.lower() == "true":
                        obj[key] = True
                    elif value.lower() == "false":
                        obj[key] = False
                elif isinstance(value, (list, dict)):
                    missing_data_count += recursive_check_and_format(value, current_path)
                current_path.pop()

        return missing_data_count

    # Fonction pour vérifier si une chaîne représente un nombre et le convertir
    def convert_to_number(value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    missing_data_count = recursive_check_and_format(data)
    
    if missing_data_count > 0:
        print(f"There are {missing_data_count} missing values in the JSON file.")
        # Écrire les données formatées dans le répertoire ../out
        formatted_file_path = os.path.join('..', 'out', os.path.basename(json_file).replace('.json', '_formatted.json'))
        with open(formatted_file_path, 'w') as formatted_f:
            json.dump(data, formatted_f, indent=4)
        print(f"Formatted data written to {formatted_file_path}")
    else:
        print("No missing values in the JSON file.")

def main():
    if len(sys.argv) < 4:
        print("Usage: python verification.py <file_path> <file_format> <action>")
        print("<action> can be 'check' to only check or 'format' to check and format")
        return

    file_path = sys.argv[1]
    file_format = sys.argv[2]
    action = sys.argv[3]

    if file_format == 'csv':
        if action == 'check':
            check_csv_file(file_path)
        elif action == 'format':
            check_csv_file_and_format_csv(file_path)
        else:
            print("Invalid action. Use 'check' or 'format'.")
    elif file_format == 'json':
        if action == 'check':
            check_missing_data_json(file_path)
        elif action == 'format':
            check_missing_data_and_format_json(file_path)
        else:
            print("Invalid action. Use 'check' or 'format'.")
    else:
        print("Invalid file format")

if __name__ == "__main__":
    main()