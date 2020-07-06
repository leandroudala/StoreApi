from .. import db
import datetime

from sqlalchemy.dialects.mysql import INTEGER, CHAR

class BlacklistToken(db.Model):
    __tablename__ = 'blacklist_token'

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return f'<Token: {self.token}>'

    @staticmethod
    def check_blacklist(auth_token):
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        return False
