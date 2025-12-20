from typing import Dict, List
from flask import request as FlaskRequest
from src.database.database import db
from src.models.entities.products import Product
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_not_found import HttpNotFound

class ProductController:
  def create_product(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    validated_body = self.__validate_product_creation_request_data(body=body)

    product_name = validated_body.get('name')
    product_description = validated_body.get('description')
    product_price = validated_body.get('item_price') 
    product = Product(name=product_name, description=product_description, item_price=product_price)
    db.session.add(product)
    db.session.commit()

    response = self.__format_response(product) 
    return response


  def get_product(self, product_id: int) -> Dict:
    validated_product = self.__validate_if_product_exists(product_id)
    response = self.__format_response(validated_product)
    
    return {
      "product": response
    }
  

  def get_products(self) -> List[Product]:
    products = Product.query.all()
    formated_product_list = [self.__format_response(product) for product in products]

    if not products:
      raise HttpNotFound("produto não encontrado")
    
    return {
      "products": formated_product_list,
      "total": len(formated_product_list)
    } 

  def update_product(self, request: FlaskRequest, product_id: int) -> Dict: # type: ignore
    body = request.json
    validated_body = self.__validate_product_creation_request_data(body=body)
    product = self.__validate_if_product_exists(product_id)
    
    product.name = validated_body.get('name')
    product.description = validated_body.get('description')
    product.item_price = validated_body.get('item_price')

    db.session.commit()
    return {"message": "produto atualizado com sucesso"}
    
  def delete_product(self, product_id: int) -> Dict:
    product_to_be_deleted = self.__validate_if_product_exists(product_id)
    db.session.delete(product_to_be_deleted)
    db.session.commit()
    return {"message": "produto deletado com sucesso"}
    
  def __validate_if_product_exists(self, product_id: int) -> Product:
    product = Product.query.get(product_id)
    if not product:
      raise HttpNotFound("produto não encontrado")
    
    return product
  

  def __validate_product_creation_request_data(self, body: Dict) -> Dict:
    if "name" not in body or "description" not in body or "item_price" not in body:
      raise HttpUnprocessableEntityError("body mal formatado")
    validated_body = body
    return validated_body

  def __format_response(self, product: Product) -> Dict:
    return product.to_dict()



