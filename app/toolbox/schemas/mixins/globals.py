from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# --- BASE READ SCHEMA AVEC MIXINS ---

class TimeStampedRead(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class SoftDeleteRead(BaseModel):
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None

class IdentifiableRead(BaseModel):
    id: Optional[int] = None
