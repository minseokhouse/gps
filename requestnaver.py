import requests

url = "http://www.naver.com"
lat = 37.1234
lng = 127.7545



# Method Get

paramDict = {
        "lat" : lat,
        "lng" : lng
}

response = requests.get(url, params=paramDict)
print("status code :", response.status_code)
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



