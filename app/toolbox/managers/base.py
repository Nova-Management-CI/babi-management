from typing import Type, TypeVar, Generic
from sqlmodel import Session 

from .mixins.extensions import ExtensionsMixin
from .mixins.crud_ops import CRUDOperationsMixin

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

class ManuelManager(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType],
    CRUDOperationsMixin, 
    ExtensionsMixin
    ):
    def __init__(self, model: Type[ModelType], db: Session):  
        from ..crud.base import BaseCrud
        self.model = model
        self.db = db
        self.crud = BaseCrud(model=model, db=db)