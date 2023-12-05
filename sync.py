import requests
import json

def get_all_data(api_url, page_size):
    all_data = []

    # Effectuer une requête GET à l'API pour récupérer les données de chaque page
    page = 1
    while True:
        response = requests.get(api_url, params={"pagination[pageSize]": page_size, "pagination[page]": page})
        data = response.json()

        # Vérifier si la page est vide
        if len(data["data"]) == 0:
            break

        # Ajouter les données de la page à la liste
        all_data.extend(data["data"])
        print(f"Page {page} récupérée.")
        # Passer à la page suivante
        page += 1

    return all_data

# URL de l'API
api_url = "http://54.37.12.181:1337/api/sneakers"

# Taille de la page de pagination
page_size = 100

# Appeler la fonction pour récupérer toutes les données
all_data = get_all_data(api_url, page_size)

# Enregistrer les données dans un fichier JSON
with open("data.json", "w") as file:
    json.dump(all_data, file)

print("Les données ont été enregistrées dans le fichier data.json.")