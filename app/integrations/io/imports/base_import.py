import pandas as pd
from abc import ABC, abstractmethod

class BaseImportEngine(ABC):
    @abstractmethod
    def read(self, file_path: str) -> pd.DataFrame:
        """Chaque moteur doit retourner un DataFrame Pandas."""
        pass