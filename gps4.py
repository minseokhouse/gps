import serial
import time
import string
import pynmea2
import sys
import requests
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

pnChannel = "raspi-tracker"

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-38f9a86a-ce68-11eb-a572-a6433017f026"
pnconfig.publish_key = "pub-c-c3109ea1-29a9-494c-847b-0e4feafc5589"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)
pubnub.subscribe().channels(pnChannel).execute()


url = "http://www.naver.com"

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    if sys.version_info[0] == 3:
        newdata = newdata.decode("utf-8","ignore")
        
        if newdata[0:6] == "$GPRMC":
                print(newdata)
                newmsg=pynmea2.parse(newdata)
                lat=newmsg.latitude
                lng=newmsg.longitude
                
            
                # Method Get
                
                paramDict = {
                    "lat" : lat,
                    "lng" : lng
                }
                
                response = requests.get(url, params=paramDict)
                print("status code : ", response.status_code)
                print(response.url)
                
                
                
                # Method Post
                '''
                datas = {
                    "lat" : lat,
                    "lng" : lng
                }
                
                response = requests.post(url, data=datas)
                print("status code :", response.status_code)
                print(response.url)
                '''
                
                try:
                    envelope = pubnub.publish().channel(pnChannel).message({'lat':lat, 'lng':lng}).sync()
                    print("publish timetoken: %s" % envelope.result)
                except PubNubException as e:
                    print("error")
