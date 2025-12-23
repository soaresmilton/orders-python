from flask import Flask
from src.database.database import db
from src.models.entities.orders import Order
from src.models.entities.products import Product
from src.models.entities.order_items import OrderItems
from src.server.server import create_app

app = create_app()

if __name__ == '__main__':
  with app.app_context():
    db.drop_all()
    db.create_all()


  app.run(debug=True)