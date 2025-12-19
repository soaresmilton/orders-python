from flask import request, jsonify, Blueprint
from src.models.entities.products import Product
from src.factories.product_factory import product_factory
from src.errors.error_controller import handle_errors

products_bp = Blueprint('products_routes', __name__)

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
  pass


@products_bp.route('/products', methods=['POST']) # type: ignore
def create_product():
  try:
    product = product_factory()
    created_product = product.create_product(request)
    return jsonify(created_product)
  except Exception as exception:
    error_response  = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]

  