from fastapi import APIRouter

from ..models.preference import UserPreference
from ..schemas.preference import UserPreferenceRead, UserPreferenceUpdate
from app.common import PREFIX, TAGS, FEATURES, STATUS

#=================TAG COMMON=================
PREFIX=PREFIX.ACCOUNT_CUSTOM
FEATURES=FEATURES.ACCOUNT_CUSTOM
STATUS=STATUS.OK

def get_user_preferences_auto_router() -> APIRouter:
    from app.toolbox import BaseCrud, AutoRouter
    
    TAGS=["User-Preferences"]
    return AutoRouter(
        model_crud=BaseCrud(UserPreference),
        schema_read=UserPreferenceRead,
        schema_update=UserPreferenceUpdate,
        prefix=f"{PREFIX}/preferences",
        tags=TAGS,
        allow_me=True,  # Permet d'accéder/modifier directement ses propres préférences (/me)
        required_feature=FEATURES
    ).router


# Liste groupée à importer dans ton fichier global `all_routers`
custom_preference_routers = [
    get_user_preferences_auto_router,
]
