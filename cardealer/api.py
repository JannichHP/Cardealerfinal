import urllib.request, urllib.parse, urllib.error
import json

print("Enter registration:")
registration=input


#Pulls data from the given api url
ApiUrl = "http://api.nrpla.de/"
url = ApiUrl + registration() +"?api_token=iZ3T9knspElwMyglvXbFKaKXK8co5k0LKjLzke6Uirnaw5FuqtE20SXKI4ttrZIM&advanced=1"    

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()


#Makes it so only the three items ("brand"-"engine") are selected from the api
js=json.loads(data)
brand = js["data"]["brand"]
model = js["data"]["model"]
engine = js["data"]['version']

print("Brand:", brand)
print("model:", model)
print("version:", engine)