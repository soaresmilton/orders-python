from src.controllers.product_controller import ProductController
from src.repositories.product_repository import ProductRepository

def product_factory() -> ProductController:
  repository = ProductRepository()
  return ProductController(repository)