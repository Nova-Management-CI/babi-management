from fastapi import APIRouter

from ..schemas.stock import (
    INVStockOutputCreate,INVStockReceptionCreate,
    INVStockAdjustmentCreate,
)
from ..managers.main import InventoryManager
from app.common import PREFIX, TAGS, FEATURES, STATUS

# ==================================MANUAL ROUTERS (Actions métier spécifiques via Managers)=======================================

POST="POST"
STATUS=STATUS.OK

def get_inventory_manual_router() -> APIRouter:
    from app.toolbox import  ManuelRouter, ManagerFactory
        
    FEATURES=FEATURES.INVENTORY
    PREFIX=f"{PREFIX.INVENTORY}/gestion"
    TAGS= ["Gestion Stocks"]

    MANAGER = ManagerFactory.get_manager(InventoryManager)
    manual_router = ManuelRouter(
        manager_cls=MANAGER,prefix=PREFIX,
        tags=TAGS,required_feature=FEATURES
    )
    P="/receive"
    manual_router.add(
        path=P,method=POST,
        action_name="receive_stock",
        response_model= INVStockReceptionCreate
    )
    P="/output"

    manual_router.add(
        path=P,method=POST,
        action_name="register_output",status_code=STATUS,
        response_model=INVStockOutputCreate
    )
    P="/adjust"
    manual_router.add(
        path=P,method=POST,
        action_name="adjust_stock",status_code=STATUS,
        response_model=INVStockAdjustmentCreate,
    )

    return manual_router.router

manuel_routers = [
    get_inventory_manual_router,
    
]
