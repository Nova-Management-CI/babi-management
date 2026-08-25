from fastapi import APIRouter

# --- Modèles et Schémas ---

from ..schemas.profil  import(
   OrgTenantCreate
)
from ..managers.main import OrgManager
from app.common import PREFIX, TAGS, FEATURES, STATUS

#================================== MANUAL ROUTERS (Actions métier spécifiques via Managers)=======================================

FEATURES=FEATURES.ORG_IDENTITY
PREFIX=f"{PREFIX.ORG_IDENTITY}/tenant"
TAGS=["Tenant Infos"]
POST="POST"
PATCH="PATCH"
STATUS=STATUS.OK


def get_org_manuel_router() -> APIRouter:
    from app.toolbox import  ManuelRouter, ManagerFactory

    org_manager = ManagerFactory.get_manager(OrgManager)

    manual_router = ManuelRouter(
        manager_cls=org_manager,prefix=PREFIX,tags=TAGS, required_feature=FEATURES
    )

    PATH="/register"
    manual_router.add(
        path=PATH,method=POST,
        action_name="register_full_organization",
        response_model= OrgTenantCreate
    )
    return manual_router.router

manuel_routers = [
    get_org_manuel_router
]

