import requests
import os
from gtts import gTTS
from time import sleep

def playTemp():
    dataa = requests.get("https://api.weatherapi.com/v1/current.json?q=V5R&key=dc065743d1ee4ff1b37161302231606&lang=%2Fapplication.json").json()
    text = "The temperature right now is " + str(dataa.get("current").get("temp_c")) + "celcius, it is currently " + str(dataa.get("current").get("condition").get("text")) + ". The wind is currently " + str(dataa.get("wind_kph")) + " kilometers per hour and it is travelling at" + str(dataa.get("wind_degree"))
    gTTS(text=text,lang="en",slow=False,tld="co.uk").save("temperature.mp3")
    os.system("start temperature.mp3")
    sleep(15)
    playTemp()
playTemp()
