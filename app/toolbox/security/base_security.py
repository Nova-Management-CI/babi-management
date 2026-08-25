from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# tokenUrl pointe vers l'authentification Firebase (ou peut rester symbolique)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class SecurityManager:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # --- Gestion des Mots de Passe ---
    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
security=SecurityManager()