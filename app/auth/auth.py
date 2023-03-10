from http import HTTPStatus

from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from ..models import User
from app.errors.error_handlers import APIError

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    print(username, password)
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    raise APIError('Ошибка аутентификации', HTTPStatus.UNAUTHORIZED)


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():
    raise APIError('Ошибка аутентификации', HTTPStatus.UNAUTHORIZED)
