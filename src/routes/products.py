from flask import request, jsonify, Blueprint
from src.models.entities.products import Product
from src.factories.product_factory import product_factory
from src.errors.error_controller import handle_errors

products_bp = Blueprint('products_routes', __name__)

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
  try:
    product_controller = product_factory()
    product = product_controller.get_product(product_id)
    return product
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]

@products_bp.route('/products', methods=['POST']) # type: ignore
def create_product():
  try:
    product_controller = product_factory()
    created_product = product_controller.create_product(request)
    return jsonify(created_product)
  except Exception as exception:
    error_response  = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]

@products_bp.route('/products', methods=['GET']) # type: ignore
def get_products():
  try:
    product_controller = product_factory()
    products_list = product_controller.get_products()
    return jsonify(products_list)
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]


  