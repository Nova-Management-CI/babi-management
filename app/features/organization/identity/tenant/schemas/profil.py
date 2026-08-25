from typing import Optional
from app.toolbox import BaseSchema
from ....subscription.billing.schemas.billing import OrgBillingCreate
from .infos import OrgInfosCreate
from app.features.account.identity.admin.schemas.admin import UserAdminCreate

class OrgTenantCreate(BaseSchema):
    infos: "OrgInfosCreate"
    admin: "UserAdminCreate"
    subscription: "OrgBillingCreate"


OrgTenantCreate.model_rebuild()


