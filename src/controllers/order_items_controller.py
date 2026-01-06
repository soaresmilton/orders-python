from typing import Dict
from src.models.entities.order_items import OrderItems
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_not_found import HttpNotFound
from src.repositories.order_items_repository import OrderItemsRepository

class OrderItemsController:
  def __init__(self, repository: OrderItemsRepository):
    self._repository = repository

  def create_order_item(self, body: Dict) -> Dict:
    validated_body = self.__validate_order_item_request_data(body)

    order_item = OrderItems(
      order_id=validated_body["order_id"],
      item_id=validated_body["item_id"],
      item_price=validated_body["item_price"],
      quantity=validated_body["quantity"]
    )

    save_order_item = self._repository.save(order_item)
    response = save_order_item.to_dict()

    return response
  

  def __validate_order_item_request_data(self, body: Dict) -> Dict:
    if "order_id" not in body or "item_id" not in body or "item_price" not in body or "quantity" not in body:
      raise HttpUnprocessableEntityError('body mal formatado')
    validated_body = body
    return validated_body
    