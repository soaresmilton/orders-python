from datetime import datetime
from src.database.database import db

class Orders(db.Model):
  __tablename__ = "orders"
  
  id = db.Column(db.Integer, primary_key=True)
  order_item_id = db.Column(db.Integer, nullable=False)
  total_price = db.Column(db.Float, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  status = db.Column(db.String(80), nullable=False, default='CREATED')