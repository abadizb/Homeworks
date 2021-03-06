import urllib.request
from urllib.error import URLError
import json
import time

def weather(query):
    weather_query=''
    for items in query:
        weather_query=weather_query+str(items)+' '
    try:
        urlwebsite = "http://api.openweathermap.org/data/2.5/weather?q=west%20haven,%20ct="+weather_query
        page = urllib.request.urlopen(urlwebsite)

        pagecode = page.getcode()
        if pagecode==200:
            content=page.read()
            content_string = content.decode("utf-8")

            json_data = json.loads(content_string)

            print ("\n"+"_________________________________")
            print("Weather update for: ",json_data["name"]+",",json_data["sys"]["country"])
            print ("Sky: ",json_data["weather"][0]["description"])
            temp = ((float(json_data["main"]["temp"]) -273.15)*(9/5))+32
            print ("Temperature: %.2f 'F" %(temp))
            print ("Humidity: {}%".format(json_data["main"]["humidity"]))
            print ("Wind: {}mph".format(json_data["wind"]["speed"]))

            print ("Sunrise: ", (time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(int(json_data["sys"]["sunrise"])))))
            print ("Sunset: ", (time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(int(json_data["sys"]["sunset"])))))
            print ("_________________________________")
    except:
        print("No weather update for "+weather_query,"\n")
