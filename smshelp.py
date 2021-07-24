import base64
import hashlib
import hmac
import time
import requests
import json

def make_signature(string):
    secret_key = bytes("iiP7U0sqph3glBH1rCJXizgNlut1O5Msy46EOhhC", 'UTF-8')
    string = bytes(string, 'UTF-8')
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode('UTF-8')
    return string_base64

message = "Hello This is python test   hangle i an dae yo. I am Minseok"
phone = "01038624194"
url = "https://sens.apigw.ntruss.com"
uri = "/sms/v2/services/" + "ncp:sms:kr:270154268312:gpshelp" + "/messages"
api_url = url + uri
timestamp = str(int(time.time() * 1000))
access_key = "xJ8jC4LIUsc5XZH3KQ5T"
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
        "from": "01038624194",
        "content": message,
        "messages": [{"to": phone}]
}

body = json.dumps(body)

response = requests.post(api_url, headers=headers, data=body)
response.raise_for_status()

