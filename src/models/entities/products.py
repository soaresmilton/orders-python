from src.database.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from typing import Dict

class Product(db.Model):
  __tablename__ = 'products'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(80), nullable=False)
  description: Mapped[str] = mapped_column(String(100), nullable=False)
  item_price: Mapped[float] = mapped_column(Float, nullable=False)


  def to_dict(self) -> Dict:
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "item_price": self.item_price
    }

 


