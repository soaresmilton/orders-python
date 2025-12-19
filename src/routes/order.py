from flask import request , jsonify, Flask, Blueprint
from src.models.entities.orders import  Orders

orders_bp = Blueprint('orders_routes', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
  req = request.json
  return req