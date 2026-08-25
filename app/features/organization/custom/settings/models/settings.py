from sqlmodel import   Relationship,Field
from typing import Optional, List,TYPE_CHECKING

from app.toolbox import (
     BaseTenant
)

class OrgSettings(BaseTenant, table=True):
    __tablename__ = "org_settings"
    
    sms_balance: int = Field(default=0)
    is_setup_completed: bool = Field(default=False)
    
    org: Optional["Organization"]  = Relationship(back_populates="settings")
