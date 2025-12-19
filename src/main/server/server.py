from flask import Flask
from src.main.routes.orders import orders_route_bp

app = Flask(__name__)

app.register_blueprint(orders_route_bp)