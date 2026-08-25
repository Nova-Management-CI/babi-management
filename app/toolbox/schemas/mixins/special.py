from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class LifecycleSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    is_active: bool = True

class NotesDescriptionSchemaMixin(BaseModel):
    notes: Optional[str] = None
    description: Optional[str] = None