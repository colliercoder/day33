import requests
from datetime import datetime

MY_LAT = 6.244203
MY_LONG = -75.581215

parameters = { "lat" : MY_LAT, "lng" : MY_LONG, "formatted":0 }

response = requests.get('http://api.sunrise-sunset.org/json',params=parameters,verify=False)
response.raise_for_status()

data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise,sunset)
time_now = datetime.now()
print(time_now.hour)

print(data)

