import pyowm
from pyowm import OWM

owm = OWM(API_key='7500ac44cc845404cbb0f9bedf7a0e3a') # API-key

city = input(str('What city are you interested in?: '))
observation = owm.weather_at_place(city)
w = observation.get_weather() # Variables
temp = w.get_temperature('celsius')['temp']
status = w.get_status()

print('In ' + city + ' temperature:' + str(temp) + ' C°.' ) # Data output
print('Also in this city ' + status.lower())