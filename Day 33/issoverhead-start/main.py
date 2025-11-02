import requests
import smtplib
from datetime import datetime
import time

MY_LAT, MY_LONG = -22.4623917, -68.9272181 # Latitud y Longitud de calama
FROM_EMAIL = "testforpythoncourse@gmail.com"
PASSWORD = "kagf zprj ctit xjyw"
TO_EMAIL = "alvaro.hernan.orellana@gmail.com"
message = "Subject:Automated Message from alvarito✨✨✨:\n\nThe International Space Station is above you. Look up!"

def is_night_time() -> bool:
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    is_night_time = sunset >= datetime.now().hour <= sunrise
    return is_night_time

def get_iss_coordinates() -> (float, float):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude

def iss_is_overhead() -> bool:
    iss_latitude, iss_longitude = get_iss_coordinates()

    #if positions are within +5 or -5 degrees they are considered close
    delta_latitude = abs(iss_latitude - MY_LAT)
    delta_longitude = abs(iss_longitude - MY_LONG)
    return delta_latitude <= 5 and delta_longitude <= 5

# If your position is within +5 or -5 degrees of the ISS position and if it is currently dark
# then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(FROM_EMAIL, PASSWORD)

    while True:
        time.sleep(seconds=60)
        if iss_is_overhead() and is_night_time():
            connection.sendmail(FROM_EMAIL, TO_EMAIL, message)