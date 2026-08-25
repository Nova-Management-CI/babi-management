
# --- Importation des listes de routeurs de tous les modules ---
from .stock import  gestions_routers
from .manuel import manuel_routers

# =====================================================================
# 1. CONSOLIDATION DE TOUS LES ROUTEURS DANS UNE LISTE UNIQUE
# =====================================================================

all_routers = [
    *gestions_routers,
    *manuel_routers
]

