from src.models.entities.orders import Order
from src.repositories.orders_repository import OrdersRepository
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict

class OrdersController:
  def __init__(self, repository: OrdersRepository):
    self._repository =  repository
  
  def create_order(self) -> Dict:
    order = Order()
    saved_order = self._repository.save(order)
    response = saved_order.to_dict()

    return response

  def get_order(self, order_id: int) -> Dict:
    order = self._repository.get_by_id(order_id)
    response = order.to_dict()
    return {
      "order": response
    }
  
  def get_orders(self) -> Dict:
    orders = self._repository.get_all()
    formated_orders_list = [order.to_dict() for order in orders]

    return {
      "orders": formated_orders_list,
       "total": len(formated_orders_list)
    }

  def update_order(self, body: Dict, order_id: int) -> Dict:
    validated_body = self.__validate_order_request_data(body)

    self._repository.update(order_id, validated_body)
    return {"message": "pedido atualizado com sucesso."}
  
  def delete_order(self, order_id: int) -> Dict:
    order = self._repository.get_by_id(order_id)
    self._repository.delete(order)

    return {"message": "pedido deletado com sucesso"}

  def __validate_order_request_data(self, body: Dict) -> Dict:
    if "status" not in body:
      raise HttpUnprocessableEntityError('body mal formatado')
    
    validated_body =  body
    return validated_body