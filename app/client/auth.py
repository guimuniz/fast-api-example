import base64
import hashlib
import hmac
import time

from requests.auth import AuthBase

from app.core.config import settings


class ExampleAuth(AuthBase):
    def __init__(self):
        self.api_key = settings.API_KEY
        self.secret_key = settings.SECRET_KEY
        self.passphrase = settings.PASSPHRASE

    def __call__(self, request):
        timestamp = str(int(time.time()))
        message = timestamp + request.method + str(request.url).split('.com')[1] + str(request.content or '')
        signature = hmac.new(
            self.secret_key.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256
        ).digest()
        signature_b64 = base64.b64encode(signature).decode()
        request.headers.update(
            {
                'X-CB-ACCESS-SIGNATURE': signature_b64,
                'X-CB-ACCESS-TIMESTAMP': timestamp,
                'X-CB-ACCESS-KEY': self.api_key,
                'X-CB-ACCESS-PASSPHRASE': self.passphrase,
                'Accept': 'application/json',
            }
        )
        return request
