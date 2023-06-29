from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from app.routes import auth_routes, user_routes


routes = [auth_routes, user_routes]

for route in routes:
    routes_bp.register_blueprint(route)

__all__ = ['routes_bp']
