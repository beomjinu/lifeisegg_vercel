import platform, os, requests, time, datetime, uuid, hmac, hashlib, json
from django.conf import settings
from django.utils import timezone

class Message:
    def __init__(self):
        self.default_agent = {
            'sdkVersion': 'python/4.2.0',
            'osPlatform': platform.platform() + " | " + platform.python_version()
        }

        self.url       = "https://api.solapi.com/messages/v4/send"
        self.date      = timezone.now().isoformat()
        self.salt      = str(uuid.uuid1().hex)

        self.headers = {
            'Authorization': 'HMAC-SHA256 ApiKey=' + settings.ENV_DATA['SOLAPI_CK'] + ', Date=' + self.date + ', salt=' + self.salt + ', signature=' + (hmac.new((settings.ENV_DATA['SOLAPI_SK']).encode(), (self.date + self.salt).encode(), hashlib.sha256).hexdigest()),
            'Content-Type': 'application/json; charset=utf-8'
        }

        self.templates = {
            '주문접수': 'KA01TP230701162116367VjEPEehkl6I',
            '발송완료': 'KA01TP230708122917670lqAsmIPnu7C',
            '입금요청': 'KA01TP230924104434717hRcJXTwEOKT',
            '재입금요청': 'KA01TP230924104332022LB6zegVF47h',
            '주문취소': 'KA01TP230924105546980gOo5BjJNnxm',
        }        

    def create_send_data(self, data):
        self.send_data = {
            "agent": self.default_agent,

            'message': {
                'to': data["to"],
                'from': settings.ENV_DATA['SOLAPI_NUMBER'],
                
                'kakaoOptions': {
                    'pfId': settings.ENV_DATA['SOLAPI_PFID'],
                    'templateId': self.templates[data["template"]],
                    'variables': data["var"]
                }
            }
        }
    
    def send(self):
        return requests.post(self.url, headers=self.headers, json=self.send_data)