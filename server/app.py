from sanic import Sanic

from api import api_bp

app = Sanic('qspace')

app.blueprint(
    api_bp,
)
