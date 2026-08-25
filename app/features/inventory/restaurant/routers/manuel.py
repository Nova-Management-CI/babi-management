from fastapi import APIRouter

from ..schemas.restaurant import (
    OrderCreate,
)
from ..managers.main import RestaurantManager
from app.common import PREFIX, TAGS, FEATURES, STATUS

# ==================================MANUAL ROUTERS (Actions métier spécifiques via Managers)=======================================


POST="POST"
STATUS=STATUS.OK

def get_order_manual_router() -> APIRouter:
    from app.toolbox import  ManuelRouter, ManagerFactory
    FEATURES=FEATURES.INVENTORY
    PREFIX=f"{PREFIX.INVENTORY}/restaurant"
    TAGS=["Order Restaurant"]

    MANAGER = ManagerFactory.get_manager(RestaurantManager)
    manual_router = ManuelRouter(
        manager_cls=MANAGER,prefix=PREFIX,
        tags=TAGS,required_feature=FEATURES
    )
    P="/register"
    manual_router.add(
        path=P,method=POST,
        action_name="create_order",
        response_model= OrderCreate
    )

    return manual_router.router

manuel_routers = [
    get_order_manual_router,
    
]
