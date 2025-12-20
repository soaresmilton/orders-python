from src.database.database import db
from src.models.entities.products import Product
from typing import Dict, List
from src.errors.http_not_found import HttpNotFound

class ProductRepository:
  def save(self, product: Product) -> Product:
    db.session.add(product)
    db.session.commit()

    return product

  def get_by_id(self, product_id: int) -> Product:
    product = Product.query.get(product_id)
    if not product:
      raise HttpNotFound("produto não encontrado")
    
    return product
  
  def get_all(self) -> List[Product]:
    products = Product.query.all()

    if not products:
      raise HttpNotFound("produto não encontrado")

    return products
  
  def update(self, product_id: int, validated_body: Dict) -> None:
    
    product = self.get_by_id(product_id)
    
    product.name = validated_body.get('name')
    product.description = validated_body.get('description')
    product.item_price = validated_body.get('item_price')

    db.session.commit()

  def delete(self, product: Product) -> None:
    db.session.delete(product)
    db.session.commit()
    