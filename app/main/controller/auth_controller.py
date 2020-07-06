from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    @api.doc('Log in user and get a token')
    @api.expect(user_auth, validate=True)
    def post(self):
        return Auth.login_user(data=request.json)

@api.route('/logout')
class UserLogout(Resource):
    @api.doc('Log out a user')
    def post(self):
        return Auth.logout_user(data=request.headers.get('Authorization'))
