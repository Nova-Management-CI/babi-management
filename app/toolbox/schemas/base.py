from pydantic import BaseModel,ConfigDict
from .mixins.globals  import (
    IdentifiableRead, TimeStampedRead, SoftDeleteRead

)
class BaseGlobal(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, 
        populate_by_name=True,
        str_strip_whitespace=True,
        validate_assignment=True
    )

class BaseSchema(BaseGlobal):
    pass


class BaseReadSchema(IdentifiableRead, TimeStampedRead, SoftDeleteRead):
    pass