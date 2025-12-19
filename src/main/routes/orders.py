from flask import Blueprint, request, jsonify

orders_route_bp = Blueprint("orders_routes", __name__)

@orders_route_bp.route("/", methods=['GET']) # type: ignore
def test():
  return "Hello World"