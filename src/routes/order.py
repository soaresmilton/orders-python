from flask import request , jsonify, Flask, Blueprint
from src.factories.orders_factory import order_factory
from src.errors.error_controller import handle_errors

orders_bp = Blueprint('orders_routes', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
  try:
    order_controller = order_factory()
    order = order_controller.create_order()
    return jsonify(order), 201
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]


@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
  try:
    order_controller = order_factory()
    order = order_controller.get_order(order_id)
    return jsonify(order)
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]
  

@orders_bp.route('/orders', methods=['GET'])
def ger_orders():
  try:
    order_controller = order_factory()
    orders_list = order_controller.get_orders()
    return jsonify(orders_list)
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]


@orders_bp.route('/orders/<int:order_id>', methods=["PUT"])
def update_order(order_id):
  try:
    body = request.json
    order_controller = order_factory()
    response = order_controller.update_order(body, order_id)
    return jsonify(response)
  except Exception as exception:
    error_response = handle_errors(exception)
    return jsonify(error_response["body"]), error_response["status_code"]