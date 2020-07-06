from flask_restplus import Api
from flask import Blueprint

from app.main.controller.user_controller import api as user_ns
from app.main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title="Store API",
    version='1.0',
    description="Store API helps sales and stock management"
)

api.add_namespace(user_ns)
api.add_namespace(auth_ns)
