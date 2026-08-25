import firebase_admin
from firebase_admin import credentials, auth
from pathlib import Path

# Chemin vers ton fichier JSON de clé privée
cred_path = Path(__file__).resolve().parent / "firebase-service-account.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(str(cred_path))
    firebase_admin.initialize_app(cred)

def verify_firebase_token(id_token: str):
    """
    Vérifie le jeton JWT envoyé par le client et retourne les informations (dont le uid).
    """
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None