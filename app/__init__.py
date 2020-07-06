from flask_restplus import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title="Store API",
    version='1.0',
    description="Store API helps sales and stock management"
)
