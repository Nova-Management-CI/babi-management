from fastapi import APIRouter

from ...user.models.infos import UserInfos
from ..schemas.admin import ProfileAdminRead, ProfileAdminUpdate
from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ACCOUNT_IDENTITY
FEATURES=FEATURES.ACCOUNT_IDENTITY
STATUS=STATUS.OK

def get_admin_auth_auto_router() -> APIRouter:
    from app.toolbox import BaseCrud, AutoRouter
    
    TAGS = ["Identity-Admin"]
    MODELE_SQL = BaseCrud(UserInfos)

    return AutoRouter(
        model_crud=MODELE_SQL,
        schema_read=ProfileAdminRead,
        schema_update=ProfileAdminUpdate,
        prefix=f"{PREFIX}/admin",
        tags=TAGS,
        required_feature=FEATURES,
        allow_me=True,
    ).router


profil_admin_routers = [
    get_admin_auth_auto_router,
]
