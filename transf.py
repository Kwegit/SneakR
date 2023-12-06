import json
import csv
import pandas as pd

# Lire les données à partir du fichier JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Créer un DataFrame à partir des données
df = pd.DataFrame(data)

# Diviser la colonne "attributes" en plusieurs colonnes
attributes_df = pd.json_normalize(df["attributes"])

# Fusionner les DataFrames
merged_df = pd.concat([df.drop("attributes", axis=1), attributes_df], axis=1)

# Définir le chemin du fichier TSV de sortie
tsv_file = "data.tsv"

# Écrire les données dans le fichier TSV
merged_df.to_csv(tsv_file, sep="\t", index=False)

print("Le fichier data.json a été converti en data.tsv avec succès.")