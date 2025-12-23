from src.database.database import db
from src.models.entities.orders import Order
from typing import Dict, List
from src.errors.http_not_found import HttpNotFound

class OrdersRepository:
  def save(self, order: Order) -> Order:
    db.session.add(order)
    db.session.commit()

    return order

  def get_by_id(self, order_id: int) -> Order:
    order = Order.query.get(order_id)
    if not order:
      raise HttpNotFound("pedido não encontrado")
    
    return order
  

  def get_all(self) -> List[Order]:
    orders = Order.query.all()

    if not orders:
      raise HttpNotFound("ordens não encontradas")

    return orders
  
  def update(self, order_id: int, validated_body: Dict) -> None:
    order = self.get_by_id(order_id)

    order.status = validated_body.get('status')

    db.session.commit()


  def delete(self, order: Order) -> None:
    db.session.delete(order)
    db.session.commit()