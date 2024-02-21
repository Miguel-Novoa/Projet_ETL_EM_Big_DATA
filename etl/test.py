import pandas as pd

# Lire le fichier CSV
df = pd.read_csv('../in/titanic.csv')

# Sélectionner les 50 premières lignes
df_50 = df.head(50)

# Réécrire les 50 premières lignes dans un nouveau fichier CSV
df_50.to_json('../out/titanic_50.json', index=False)
