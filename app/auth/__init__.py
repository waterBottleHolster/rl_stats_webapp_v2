# this file is where the 'main' blueprint is created

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views