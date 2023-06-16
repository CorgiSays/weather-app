import requests
import os
from gtts import gTTS

dataarcadi = requests.get("https://api.weatherapi.com/v1/current.json?q=V5R&key=dc065743d1ee4ff1b37161302231606&lang=%2Fapplication.json").json()
text = "The temperature right now is " + str(dataarcadi.get("current").get("temp_c"))

gTTS(text=text,lang="en",slow=False).save("temperature.mp3")
os.system("start temperature.mp3")