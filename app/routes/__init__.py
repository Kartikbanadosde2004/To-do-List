from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
main_bp = Blueprint('main', __name__)

from app.routes import auth_routes, main_routes, task_routes  # noqa
