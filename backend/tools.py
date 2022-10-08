from datetime import datetime, timedelta
import jwt
from django.db import connection

JWT_SECRET_KEY = "123"


def get_jwt(username, role_data='default'):
    # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生payload部分的方法
    # payload = jwt_payload_handler(user)  # 生成payload, 得到字典
    #
    # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 生成jwt的方法
    # print(jwt.decode(token,JWT_SECRET_KEY))
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username, 'role_data': role_data}
    }

    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    print(token)
    print(jwt.decode(token, JWT_SECRET_KEY))
    return str(token)


def check_user(username, password):
    with connection.cursor() as cursor:
        sql = 'select * from user_account where CodeName = \'' + username + "\'"
        try:
            cursor.execute(sql)
            one = cursor.fetchone()
            result = (one[1] == password)
        except:
            print('false')
            return False
    return result, one[0], one[2]


def judge(token, std):
    test = str.encode(token)[2:-1]
    try:
        result = jwt.decode(test, JWT_SECRET_KEY, algorithms='HS256')
        name = result.get('data').get('username')
    except:
        return False
# print(payload.get('data'))
