from sqlmodel import Session, select
from ..models.restaurant import Order, OrderItem
from ..schemas.restaurant import OrderCreate


class OrderManager:
    def __init__(self):
        self.Order = BaseCrud(Order)

    async def create_order(self, db, order_data: OrderCreate) -> Order:
        # 1. Créer l'objet Order principal
        db_order = Order(
            location_reference=order_data.location_reference,
            status="PENDING",
            preparation_status="PENDING",
            total_amount=0.0
        )
        self.db.add(db_order)
        self.db.refresh(db_order)

        total_amount = 0.0
        """

        # 2. Parcourir les articles commandés et les rattacher
        for item_data in order_data.items:
            # Récupérer le variant pour obtenir son prix de vente actuel
            variant = self.db.get(Variant, item_data.variant_id)
                raise ValueError(f"Variant avec l'id {item_data.variant_id} introuvable.")

            unit_price = variant.selling_price
            line_total = unit_price * item_data.quantity
            total_amount += line_total

            db_item = OrderItem(
                order_id=db_order.id,
                variant_id=item_data.variant_id,
                quantity=item_data.quantity,
                unit_price=unit_price,
                notes=item_data.notes
            )
            self.db.add(db_item)

        # 3. Mettre à jour le montant total de la commande
        db_order.total_amount = total_amount
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)"""

        return db_order