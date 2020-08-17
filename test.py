import json

from db_config import db


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return{'username': self.username, 'email': self.email}

    @staticmethod
    def get_all_users():
        return [User.json(user) for user in User.query.all()]

    @staticmethod
    def get_user(_username):
        query = User.query.filter_by(username=_username).first()
        return query

    @staticmethod
    def add_user(_username, _email):
        new_user = User(username=_username, email=_email)
        db.session.add(new_user)
        db.session.commit()

   