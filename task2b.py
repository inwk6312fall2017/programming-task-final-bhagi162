import unittest
from weather import Weather

weather = Weather()
# Lookup via location name.
print('enter a city:')
x=input('')
location = weather.lookup_by_location(x)
condition = location.condition()
print (condition['text'])



# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
    print (forecasts['high'])
    print (forecasts['low'])
    
    if (forecasts['text'])== 'Showers':
      print (forecasts['date'])
