import math
from typing import Any
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.toolbox import ManuelManager

from ..models.stock import Stock, StockHistory
from ...catalog.models.catalog import Variant

from ..schemas.stock import INVStockAdjustmentCreate

class StockOutput:

    async def adjust_stock(self, data: INVStockAdjustmentCreate):
        """Ajuste manuellement l'inventaire (Async)."""
        stock_stmt = select(Stock).where(Stock.variant_id == data.variant_id)
        stock_result = await self.db.execute(stock_stmt)
        stock = stock_result.scalars().first()
        
        if not stock:
            raise HTTPException(status_code=404, detail="Ligne de stock introuvable pour ce produit")

        old_total = stock.total_quantity
        new_total = data.new_quantity_loose + (data.new_quantity_cartons * stock.quantity_by_carton)
        diff = new_total - old_total
        
        stock.quantity_loose = data.new_quantity_loose
        stock.quantity_cartons = data.new_quantity_cartons
        
        self.db.add(StockHistory(
            variant_id=data.variant_id, 
            movement_type="ADJUSTMENT", 
            quantity=diff, 
            comment=f"Correction d'inventaire: {data.comment}"
        ))
        self.db.add(stock)
        await self.db.refresh(stock)
        return stock