
from app.main import db
from app.main.model.user import User

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        auth_token = User.encode_auth_token(user.id)
        return {
            'status': 'success',
            'msg': 'Successfully registered',
            'Authorization': auth_token.decode()
        }, 201

def save_new_user(data):
    user = User.query.filter_by(username=data['username']).first()

    if user:
        return {
            'status': 'fail',
            'msg': 'Username already exists.'
        }, 409

    new_user = User(
        name=data['name'],
        username=data['username'],
        password=data['password']
    )
    save_changes(new_user)
    return generate_token(new_user)

def get_all_users():
    return User.query.all()

def get_user(id):
    return User.query.filter_by(id=id).first()
