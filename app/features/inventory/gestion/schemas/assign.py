from typing import Optional

from app.toolbox import BaseSchema, BaseReadSchema
from app.features.account.identity.user.schemas.infos import ProfileInfosNested

# ================================STOREKEEPER===========================


class ProfileStoreKeeperBase(BaseSchema):
    can_approve_requests: Optional[bool] = None


class ProfileStoreKeeperCreate(ProfileStoreKeeperBase):
    pass


class ProfileStoreKeeperUpdate(ProfileStoreKeeperBase):
    can_approve_requests: Optional[bool] = None


class ProfileStoreKeeperRead(ProfileStoreKeeperBase):
    user: Optional["ProfileInfosNested"]


class ProfileStoreKeeperNested(BaseReadSchema, ProfileStoreKeeperBase):
    user: Optional["ProfileInfosNested"]
