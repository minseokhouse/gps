import base64
import hashlib
import hmac
import time
import requests
import json

def make_signature(string):
    secret_key = bytes("iiP7U0sq중요키*** 일부 숨김", 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64

message = "보내는 메시지"
phone = "수신번호"
url = "https://sens.apigw.ntruss.com"
uri = "/sms/v2/services/" + "ncp:sms:kr:2701중요키*** 일부 숨김:gpshelp" + "/messages"
api_url = url + uri
timestamp = str(int(time.time() * 1000))
access_key = "xJ8jC4L중요키*** 일부 숨김"
string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + access_key
signature = make_signature(string_to_sign)

    
headers = {
        'Content-Type': "application/json; charset=UTF-8",
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signature
}
 
body = {
        "type": "SMS",
        "contentType": "COMM",
        "from": "등록된 번호",
        "content": message,
        "messages": [{"to": phone}]
}
 
body = json.dumps(body)

response = requests.post(api_url, headers=headers, data=body)
response.raise_for_status()

