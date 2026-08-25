from fastapi import APIRouter

# --- Modèles et Schémas ---
from ..schemas.infos  import(
    OrgInfosUpdate,OrgInfosRead
)
from ..models.infos import OrgInfos
from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ORG_IDENTITY
FEATURES=FEATURES.ORG_IDENTITY
STATUS=STATUS.OK

#==================================AUTO ROUTERS (Gestion CRUD standard, /export et auto-gestion)=======================================

def get_tenant_auto_router() -> APIRouter:

    from app.toolbox import BaseCrud, AutoRouter
    MODELE_SQL=BaseCrud(OrgInfos)
    TAGS=["Tenant Infos"]

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_update=OrgInfosUpdate,
        schema_read=OrgInfosRead,
        prefix=f"{PREFIX}/tenant",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=True,
    ).router

# =====================================================================
# LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================

identity_tenant_routers = [
    get_tenant_auto_router,
]