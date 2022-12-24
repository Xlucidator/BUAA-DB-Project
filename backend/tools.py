from datetime import datetime, timedelta
import jwt
from django.db import connection
from django.http import JsonResponse

JWT_SECRET_KEY = "123"


def get_jwt(username, role_data='default'):
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username, 'role_data': role_data}
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return str(token)


def token2name(token):
    test = str.encode(token)[2:-1]
    result = jwt.decode(test, JWT_SECRET_KEY, algorithms='HS256', options={"verify_signature": False})
    return result.get('data').get('username')


def fail(temp):
    return {'details': temp}
