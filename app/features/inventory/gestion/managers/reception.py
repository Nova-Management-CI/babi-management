import math
from fastapi import HTTPException
from sqlmodel import select

from ..models.stock import Stock, StockHistory
from ...catalog.models.catalog import Variant

from ..schemas.stock import INVStockReceptionCreate

class StockReception:
    
    async def receive_stock(self, data: INVStockReceptionCreate):
        """Réception de stock avec gestion des cartons et vrac (Async & ManuelManager)."""
        statement = select(Variant).where(Variant.id == data.variant_id)
        result = await self.db.execute(statement)
        variant = result.scalars().first()
        
        if not variant:
            raise HTTPException(status_code=404, detail="Variante de produit introuvable")

        stock_stmt = select(Stock).where(Stock.variant_id == data.variant_id)
        stock_result = await self.db.execute(stock_stmt)
        stock = stock_result.scalars().first()
        
        if not stock:
            stock = Stock(
                variant_id=data.variant_id, 
                quantity_cartons=0.0, 
                quantity_loose=0.0,
                quantity_by_carton=data.units_per_carton
            )
            self.db.add(stock)
        
        stock.quantity_cartons += data.cartons
            
        units_per_c = stock.quantity_by_carton or data.units_per_carton
        total_received_units = (data.cartons * units_per_c)

        history = StockHistory(
            variant_id=data.variant_id,
            movement_type="IN",
            quantity=total_received_units,
            comment=f"Réception: { data.comment or 'Aucun commentaire'}"
        )
        self.db.add(history)
        await self.db.refresh(stock)
        return stock
        