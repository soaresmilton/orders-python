from src.controllers.orders_controller import OrdersController
from src.repositories.orders_repository import OrdersRepository

def order_factory() -> OrdersController:
  repository = OrdersRepository()
  return OrdersController(repository)
