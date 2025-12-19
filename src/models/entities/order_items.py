from src.database.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, DateTime
from datetime import datetime
from typing import Dict

class OrderItems(db.Model):
  __tablename__ = 'order_items'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  order_id: Mapped[int] = mapped_column(Integer)
  item_id: Mapped[int] = mapped_column(Integer)
  quantity: Mapped[float] = mapped_column(Float)
  created_at: Mapped[DateTime] =  mapped_column(DateTime, default=datetime.now)

  def to_dict(self) -> Dict:
    return {
    "id": self.id, 
    "order_id":self.order_id,
    "item_id": self.item_id,
    "quantity": self.quantity,
    "created_at": self.created_at
    }
 


