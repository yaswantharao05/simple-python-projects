import time
import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 13.105770
MY_LONGITUDE = 80.169040

gmail_id = 'username@gmail.com'
gmail_password = 'Y1qYe(!dCLU%f7'


def iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5) and (MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5):
        return True
    return False


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now <= sunrise:
        return True
    return False


# If the ISS is close to my current position
# And it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if iss_overhead() and is_night():
        time.sleep(60)
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=gmail_id, password=gmail_password)
        connection.sendmail(
            from_addr=gmail_id,
            to_addrs='username@gmail.com',
            msg='Subject: ISS is Above You Right Now!\n\nInternational Space Station is passing above you right. Go '
                'watch it!!'
        )

