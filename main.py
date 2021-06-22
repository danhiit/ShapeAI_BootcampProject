# This is a project submitted to ShapeAI bootcamp

# imports
import requests
import datetime

# Parameters to be changed as per your need
api_key = '60f19fa5bfa5ba8b65451cc3d4f6522b' # This is my API Key you can use your own key
location = input("Enter the city name: ")

api_address = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api_key

api_link = requests.get(api_address)

api_response = api_link.json()

temp_city = ((api_response['main']['temp'])-273.15)
weather_desc = api_response['weather'][0]['description']
humidity = api_response['main']['humidity']
wind_speed = api_response['wind']['speed']
date_time = datetime.datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print('---------------------------------------------------------')
print('Weather Stats for -{} || {}'.format(location.upper(),date_time))
print('---------------------------------------------------------')

print('Current temperature is                    : {:.2f} deg Celsius'.format(temp_city))
print('Current weather desc                      :',weather_desc)
print('Current humidity                          : ',humidity)
print('Current wind speed is                     : {:.2f} kmph'.format(wind_speed))

with open('ShapeAI_Project1.txt','wt') as f:
    f.write('---------------------------------------------------------\n')
    f.write('Weather Stats for -{} || {}'.format(location.upper(), date_time)+'\n')
    f.write('---------------------------------------------------------\n\n')

    f.write('Current temperature is                    : {:.2f} deg Celsius'.format(temp_city)+'\n')
    f.write('Current weather desc                      : '+weather_desc+'\n')
    f.write('Current humidity                          : {}'.format(humidity)+'\n')
    f.write('Current wind speed is                     : {:.2f} kmph'.format(wind_speed))

f.close()
