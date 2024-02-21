#transform.py --> transformation pour chaques fichiers


import pandas as pd
import json

def etl_csv_to_json(csv_file, json_file):
    # Extract - Charger les données CSV dans un DataFrame
    df = pd.read_csv(csv_file)

    # Transform - Convertir le DataFrame en format JSON
    json_data = df.to_json(orient='records', lines=True)

     # Load - Sauvegarder le JSON dans un fichier
    with open(json_file, 'w') as json_output:
        json_output.write(json_data)
        
    data = []
    with open(json_file, 'r') as f:
        for line in f:
            record = json.loads(line)
            data.append(record)
            print(json.dumps(record, indent=4))

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


# Exemple d'utilisation
csv_file_path = '../in/titanic_50.csv'
json_file_path = '../out/titanic_50.json'

etl_csv_to_json(csv_file_path, json_file_path)

