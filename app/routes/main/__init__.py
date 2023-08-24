from flask import Blueprint

main = Blueprint('main', __name__)

# Import the views only after the blueprint has been created
from . import views
