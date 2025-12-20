from src.controllers.product_controller import ProductController

def product_factory() -> ProductController:
  product = ProductController()

  return product


