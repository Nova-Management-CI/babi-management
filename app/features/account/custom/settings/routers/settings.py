from fastapi import APIRouter
from app.toolbox import BaseCrud, AutoRouter
from ..models.settings import UserSetting
from ..schemas.settings import UserSettingRead, UserSettingUpdate
from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ACCOUNT_CUSTOM
FEATURES=FEATURES.ACCOUNT_CUSTOM
STATUS=STATUS.OK


def user_settings_auto_router() -> APIRouter:
    TAGS=["User-Settings"]

    return AutoRouter(
        model_crud=BaseCrud(UserSetting),
        schema_read=UserSettingRead,
        schema_update=UserSettingUpdate,
        prefix=f"{PREFIX}/settings",
        tags=TAGS,
        allow_me=True,  # Permet d'accéder/modifier directement ses propres paramètres de sécurité (/me)
        required_feature=FEATURES,
    ).router


# Liste groupée à importer dans ton fichier global `all_routers`
custom_settings_routers = [
    user_settings_auto_router,
]
