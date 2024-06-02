from flask import Blueprint

about_bp = Blueprint('about', __name__, static_folder='static', template_folder='templates')

from . import views