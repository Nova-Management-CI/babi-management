from sqlalchemy.ext.asyncio import AsyncSession
from .org import OrgTenantManager
from .togle import OrgTogleManager
from typing import Any

class OrgManager(
    OrgTenantManager,
    OrgTogleManager
    ):

    def __init__(self, db: AsyncSession):
        super().__init__(model=Any, db=db)