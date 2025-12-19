import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
_api_key = os.getenv("GEMINI_API_KEY")

if not _api_key:
    print("Erreur : Clé API introuvable dans le fichier .env")
else:
    try:
        # Initialisation sans forcer de version pour voir tout le catalogue
        client = genai.Client(api_key=_api_key)
        print("--- Modèles disponibles pour votre clé : ---")
        
        # On liste les modèles et on affiche uniquement l'attribut .name
        for m in client.models.list():
            print(f"-> {m.name}")
            
    except Exception as e:
        print(f"Erreur lors de la récupération : {e}")