from flask import Flask
from src.database.database import db
from src.models.entities.orders import Orders
from src.models.entities.products import Product
from src.server.server import create_app

app = create_app()

if __name__ == '__main__':
  with app.app_context():
    db.create_all()


  app.run(debug=True)