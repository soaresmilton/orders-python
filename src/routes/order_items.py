from flask import request, jsonify, Blueprint
from src.errors.error_controller import handle_errors


order_items_bp = Blueprint('order_items_routes', __name__)

@order_items_bp.route('/order_items', methods=['GET'])
def get_order_items():
  return "Hello order items"