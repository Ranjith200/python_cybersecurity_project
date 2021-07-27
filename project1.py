import requests,json
from datetime import datetime

api_key="dadbb8c1155971ad10ceeff83364e579"
base_url="http://api.openweathermap.org/data/2.5/weather?"
city_name=input("Enter city : ")

complete_url=base_url + "appid=" + api_key + "&q=" + city_name
response=requests.get(complete_url)
x=response.json()

date_time=datetime.now().strftime("%d %b %y")

print("-------------------------------------------------------------------------------------------------------------------")
print("Weather stats for - {} || {}".format(city_name.upper(),date_time))
print("-------------------------------------------------------------------------------------------------------------------")

if x["cod"] != "404":
	y=x["main"]
	current_temperature=y["temp"]
	current_pressure=y["pressure"]
	current_humidity=y["humidity"]
	z=x["weather"]
	weather_description=z[0]["description"]

	print("temperature (in kelvin unit) = " +
		          str(current_temperature) + " k" +
		   "\n Atmospheric pressure (in hpa unit) = " +
		          str(current_pressure) + " hpa" +
		    "\n Humidity (in percentage) = " +
		          str(current_humidity) + " %" +
		     "\n Description = " +
		          str(weather_description))


else:
	print("City Not Found!!! ")

print("=======================================================================================================================")