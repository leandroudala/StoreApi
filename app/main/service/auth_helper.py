from app.main.model.user import User
from ..service.blacklist_service import save_token

class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(username=data['username']).first()
            if user and user.check_password(data['password']):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    return {
                        'status': 'success',
                        'msg': 'User successfully logged in',
                        'Authorization': auth_token.decode()
                    }, 200
            
            return {
                'status': 'fail',
                'msg': 'Username or password does not match'
            }, 401
        except Exception as e:
            return {
                'status': "fail",
                'message': 'Something went wront. Please try again'
            }, 500

    @staticmethod
    def logout_user(data):
        if not data:
            return {
                'status': 'fail',
                'msg': 'Please provide a valid auth token'
            }, 403
        resp = User.decode_auth_token(data)

        if not isinstance(resp, str):
            return save_token(token=data), 200

        return {
            'status': 'fail',
            'msg': resp
        }, 401

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        if not auth_token:
            return {
                'status': 'fail',
                'msg': 'Please provide a valid auth token'
            }, 401

        resp = User.decode_auth_token(auth_token)
        if isinstance(resp, str):
            return {
                'status': 'fail', 
                'message': resp
            }, 401

        user = User.query.filter_by(id=resp).first()
        return {
            'status': 'success',
            'data': {
                'id': user.id,
                'username': user.username,
            }
        }, 200
