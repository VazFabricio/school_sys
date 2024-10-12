from flask import Flask, g
import os
from .db_access import Database
from .models import Base
from .routes import clientes_bp, produtos_bp, pedidos_bp

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')

    app.config['MYSQL_HOST'] = DB_HOST
    app.config['MYSQL_DATABASE'] = DB_NAME
    app.config['MYSQL_USER'] = DB_USER
    app.config['MYSQL_PASSWORD'] = DB_PASSWORD
    app.config['MYSQL_PORT'] = DB_PORT

    app.db = Database(
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DATABASE'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        port=app.config['MYSQL_PORT']
    )

    app.db.create_all() 

    # Registrando os blueprints
    app.register_blueprint(clientes_bp)
    app.register_blueprint(produtos_bp)
    app.register_blueprint(pedidos_bp)

    return app
