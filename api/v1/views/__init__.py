from flask import Blueprint

# Create the app_views variable as an instance of Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the route from index.py to add it to the app_views blueprint
from api.v1.views.index import status

