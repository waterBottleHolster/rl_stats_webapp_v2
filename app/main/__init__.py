# this file is where the 'main' blueprint is created

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors