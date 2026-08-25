from app.toolbox import(
     ExpiryMixin,UsageTrackerMixin,ApprovalMixin,BaseTenant
)
from sqlmodel import Field, Relationship
from typing import Optional, Dict, Any



class InvitationCode(BaseTenant, ApprovalMixin,ExpiryMixin, UsageTrackerMixin, table=True):
    __tablename__ = "invitation_codes"
    code: str = Field(unique=True, index=True)
    target_role: str 
    purpose: str = Field(default="RECRUITMENT")

    user: Optional["UserInfos"] = Relationship(back_populates="invitation_code")
 