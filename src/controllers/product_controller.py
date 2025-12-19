from typing import Dict
from flask import request as FlaskRequest
from src.database.database import db
from src.models.entities.products import Product

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

    response = self.__format_response(validated_body=validated_body) 
    return response


  def __validate_product_creation_request_data(self, body: Dict) -> Dict:
    if "name" not in body or "description" not in body or "item_price" not in body:
      raise Exception("body mal formatado")
    validated_body = body
    return validated_body

  def __format_response(self, validated_body: Dict) -> Dict:
    return {
      "product": {
        "name": validated_body.get('name'),
        "description": validated_body.get('description'),
        "item_price": validated_body.get('item_price')
      }
    }



