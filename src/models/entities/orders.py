from datetime import datetime
from src.database.database import db
from typing import Dict

class Order(db.Model):
  __tablename__ = "orders"
  
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String(80), nullable=False, default='CREATED')
  created_at = db.Column(db.DateTime, default=datetime.now)

  items = db.relationship("OrderItems", back_populates="order")


  def to_dict(self) -> Dict:
    return {
      "id": self.id,
      "status": self.status,
      "created_at": self.created_at.isoformat()
    }
  
  def total_price(self) -> float:
    return sum(item.subtotal() for item in self.items)