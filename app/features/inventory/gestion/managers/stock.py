import math
from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.toolbox import ManuelManager

from ..models.stock import Stock, StockHistory
from ...catalog.models.catalog import Variant

from ..schemas.stock import  INVStockOutputCreate

class RegisterOutput():

    async def register_output(self, data: INVStockOutputCreate):
        """Enregistre une sortie de stock (Async)."""
        stock_stmt = select(Stock).where(Stock.variant_id == data.variant_id)
        stock_result = await self.db.execute(stock_stmt)
        stock = stock_result.scalars().first()
        
        if not stock or (hasattr(stock.variant, "is_active") and not stock.variant.is_active):
            raise HTTPException(status_code=404, detail="Produit indisponible ou inactif")

        if stock.total_quantity < data.quantity:
            raise HTTPException(status_code=400, detail="Stock insuffisant pour honorer cette sortie")

        if stock.quantity_loose >= data.quantity:
            stock.quantity_loose -= data.quantity
        else:
            needed = data.quantity - stock.quantity_loose
            cartons_to_open = math.ceil(needed / stock.quantity_by_carton)
            
            stock.quantity_cartons -= cartons_to_open
            stock.quantity_loose = (cartons_to_open * stock.quantity_by_carton) - needed
        
        self.db.add(StockHistory(
            variant_id=data.variant_id, 
            movement_type="OUT", 
            quantity=data.quantity, 
            comment=data.comment
        ))
        self.db.add(stock)
        await self.db.refresh(stock)
        return stock
