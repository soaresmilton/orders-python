from src.database.database import db
from src.models.entities.order_items import OrderItems
from typing import Dict
from src.errors.http_not_found import HttpNotFound

class OrderItemsRepository:
  def save(self, order_item: OrderItems) -> OrderItems:
    db.session.add(order_item)
    db.session.commit()

    return order_item