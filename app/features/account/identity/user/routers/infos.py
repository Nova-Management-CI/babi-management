from fastapi import APIRouter

from ..models.infos import UserInfos

from ..schemas.infos import ProfileInfosRead, ProfileInfosUpdate
from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ACCOUNT_IDENTITY
FEATURES=FEATURES.ACCOUNT_IDENTITY
STATUS=STATUS.OK

def get_infos_auto_router() -> APIRouter:
    from app.toolbox import BaseCrud, AutoRouter
    TAGS=["Identity-User"]
    MODELE_SQL = BaseCrud(UserInfos)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=ProfileInfosRead,
        schema_update=ProfileInfosUpdate,
        prefix=f"{PREFIX}/user",
        tags=TAGS,
        required_feature=FEATURES,
        allow_export=True,
    ).router


# =====================================================================
# 3. LISTE GROUPÉE POUR LE FICHIER ALL_ROUTERS
# =====================================================================


identity_user_routers = [
    get_infos_auto_router,
    
]




