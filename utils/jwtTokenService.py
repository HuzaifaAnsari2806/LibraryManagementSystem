import datetime
import jwt

from django.conf import settings


def generate_token(email):
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
    }
    token = jwt.encode(
        payload,
        settings.JWT_KEY,
        algorithm="HS256",
    )
    return token
