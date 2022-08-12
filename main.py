import requests
from datetime import datetime,timezone
import smtplib
import time

MY_LAT = 6.244203
MY_LONG = -75.581215


#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    global MY_LAT, MY_LONG

    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude,iss_longitude)
    latmin, latmax = MY_LAT-5,MY_LAT+5
    longmin, longmax = MY_LONG-5,MY_LONG+5
    if latmin <= iss_latitude <= latmax and longmin <= iss_longitude <=longmax :
        print("ISS overhead")
        return True
    else:
        print("ISS not overhead")

def is_dark():
    global MY_LAT,MY_LONG
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc)
    hour_now = time_now.hour
    if sunrise>=hour_now>=sunset:
        print("It is dark")
        return True
    else:
        print("It is not dark.")

while True:
    time.sleep(10)
    if is_overhead() and is_dark():
        my_email = "kingreyrey2022@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password="ufdjlfdrothfmmur")
            connection.sendmail(
                from_addr=my_email,
                to_addrs="gauerked@vt.edu",
                msg="Look above!\n\nThe ISS is above your head!!"
            )
            connection.close()






