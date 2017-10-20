import unittest
from weather import Weather

weather = Weather()
# Lookup via location name.
print('enter a city:')
x=input('')
location = weather.lookup_by_location(x)
condition = location.condition()

for forecasts in location.forecast():
  if (forecasts['text'])== 'Showers':
   print (forecasts['date'])
