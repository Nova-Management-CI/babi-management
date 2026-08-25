from fastapi import APIRouter
# --- Modèles et Schémas ---
from ....identity.tenant.models.infos import (
    OrgInfos
)
from ..schemas.settings import (
   OrgSettingsRead,OrgSettingsUpdate
)

from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ORG_CUSTOM
FEATURES=FEATURES.ORG_CUSTOM
STATUS=STATUS.OK

# =====================================================================
# 1. AUTO ROUTERS (Gestion CRUD standard, import/export et auto-gestion)
# =====================================================================

    
def get_customanization_auto_router() -> APIRouter:
    from app.toolbox import BaseCrud, AutoRouter
    TAGS=["Org Settings"]
    MODELE_SQL=BaseCrud(OrgInfos)
    
    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_update=OrgSettingsUpdate,
        schema_read=OrgSettingsRead,
        prefix=f"{PREFIX}/settings",
        tags=TAGS,
        required_feature="settings",
        allow_export=True,
    ).router


# =====================================================================
# 2. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

custom_settings_routers = [
    get_customanization_auto_router,  
]

