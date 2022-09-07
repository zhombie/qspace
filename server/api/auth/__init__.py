from sanic import Blueprint

from api.auth.login import LoginView
from api.auth.logout import LogoutView

auth_bp = Blueprint('auth', url_prefix='/auth')

auth_bp.add_route(LoginView.as_view(), '/login/', name='login')
auth_bp.add_route(LogoutView.as_view(), '/logout/', name='logout')
