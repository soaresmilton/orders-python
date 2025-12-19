from flask import Flask
from src.routes.order import orders_bp
from src.routes.products import products_bp
from src.database.database import db

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "your_secret_key"
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@127.0.0.1:3306/mysql_db'

  db.init_app(app)

  app.register_blueprint(orders_bp)
  app.register_blueprint(products_bp)


  return app