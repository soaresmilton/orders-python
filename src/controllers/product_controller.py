from typing import Dict
from src.models.entities.products import Product
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_not_found import HttpNotFound
from src.repositories.product_repository import ProductRepository


class ProductController:
  def __init__(self, repository: ProductRepository):
    self._repository = repository

  def create_product(self, body: Dict) -> Dict: # type: ignore
    validated_body = self.__validate_product_creation_request_data(body=body)

    product = Product(
      name=validated_body['name'], 
      description=validated_body['description'], 
      item_price=validated_body['item_price']
      )

    saved_product = self._repository.save(product)
   
    response = self.__format_response(saved_product) 
    return response


  def get_product(self, product_id: int) -> Dict:
    validated_product = self._repository.get_by_id(product_id)
    response = validated_product.to_dict()
    
    return {
      "product": response
    }
  

  def get_products(self) -> Dict:
    products = self._repository.get_all()
    formated_product_list = [product.to_dict() for product in products]
    
    return {
      "products": formated_product_list,
      "total": len(formated_product_list)
    } 

  def update_product(self, body: Dict, product_id: int) -> Dict: # type: ignore
    validated_body = self.__validate_product_creation_request_data(body=body)

    self._repository.update(product_id=product_id, validated_body=validated_body)
    return {"message": "produto atualizado com sucesso"}
    
  def delete_product(self, product_id: int) -> Dict:
    product_to_be_deleted = self._repository.get_by_id(product_id)

    self._repository.delete(product_to_be_deleted)

    return {"message": "produto deletado com sucesso"}
    

  def __validate_product_creation_request_data(self, body: Dict) -> Dict:
    if "name" not in body or "description" not in body or "item_price" not in body:
      raise HttpUnprocessableEntityError("body mal formatado")
    validated_body = body
    return validated_body