from flask import Flask
from config import Config
from .routers.product_bp import product_bp

def inicializar_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(product_bp)
    return app