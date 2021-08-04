import serial
import time
import string
import pynmea2
import sys
import requests

 

url = "http://www.naver.com"

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    if sys.version_info[0] == 3:
        newdata = newdata.decode("utf-8","ignore")
        
        if newdata[0:6] == "$GPRMC":
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
               
