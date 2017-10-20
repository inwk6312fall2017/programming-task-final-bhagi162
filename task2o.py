import unittest
from weather import Weather

weather = Weather()
# Lookup via location name.
print('enter a city:')
x=input('')
location = weather.lookup_by_location(x)
condition = location.condition()
print (condition['text'])
for forecasts in location.forecast():
  print (forecasts['text'])
  if (forecasts['text'])== 'Showers':
   print (forecasts['date'])
