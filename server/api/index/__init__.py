from sanic import Blueprint

from api.index.index import IndexView

index_bp = Blueprint('index', url_prefix='/')

index_bp.add_route(IndexView.as_view(), '/', name='index')
