from src.database.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, DateTime
from datetime import datetime
from typing import Dict

class OrderItems(db.Model):
  __tablename__ = 'order_items'

  id =  db.Column(db.Integer, primary_key=True)
  order_id= db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
  item_id= db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
  item_price =  db.Column(db.Float)
  quantity =  db.Column(db.Float)
  created_at = db.Column(db.DateTime, default=datetime.now)

  order = db.relationship("Order", back_populates="items")
  product = db.relationship("Product")


  def to_dict(self) -> Dict:
    return {
    "id": self.id, 
    "order_id":self.order_id,
    "item_id": self.item_id,
    "item_price": self.item_price,
    "subtotal": self.subtotal,
    "quantity": self.quantity,
    "created_at": self.created_at
    }
  
  def sub_total(self) -> float:
    return self.quantity * self.item_price
 


