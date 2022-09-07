from sanic import Blueprint

from api.auth import auth_bp
from api.index import index_bp

api_bp = Blueprint.group(
    index_bp,
    auth_bp,
    # version=1
)
