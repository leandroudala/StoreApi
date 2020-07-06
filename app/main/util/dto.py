from flask_restplus import Namespace, fields

# DTO = Data Transfer Object
class UserDto:
    api = Namespace('user', description='User related operations')
    create_user = api.model('create_user', {
        'name': fields.String(description="User's name", required=True),
        'username': fields.String(description="User's username", required=True),
        'password': fields.String(description="User's password", required=True)
    })

    user = api.model('user', {
        'id': fields.Integer(description="User's identifier"),
        'name': fields.String(description="User's name"),
        'username': fields.String(description="User's username"),
        'active': fields.Integer(description="User's status (Active/Inactive)")
    })

class AuthDto:
    api = Namespace('auth', description="Authentication related operations")
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description="User's username"),
        'password': fields.String(required=True, description="User's password")
    })
