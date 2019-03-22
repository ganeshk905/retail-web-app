from flask import Blueprint

sale = Blueprint('sale', __name__)

from . import views
