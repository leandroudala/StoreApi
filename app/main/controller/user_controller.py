from flask import request
from flask_restplus import Resource

from ..service.user_service import save_new_user, get_all_users, get_user

from ..util.dto import UserDto

api = UserDto.api
_new_user = UserDto.create_user
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @api.marshal_list_with(_user, envelope='users')
    def get(self):
        return get_all_users()

    @api.response(201,'User successfully created.')
    @api.response(409,'Username already exists.')
    @api.expect(_user, validate=True)
    def post(self):
        return save_new_user(request.json)

@api.route('/<id>')
@api.param('id', "user's identifier")
@api.response(404, 'User not found')
@api.response(200, 'User found')
class User(Resource):
    @api.doc('Get a single user')
    @api.marshal_with(_user)
    def get(self, id):
        user = get_user(id)
        if user:
            return user, 200
        api.abort(404)
