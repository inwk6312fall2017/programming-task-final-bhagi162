import unittest
from weather import Weather

weather = Weather()
# Lookup via location name.
print('enter a city:')
x=input('')
location = weather.lookup_by_location(x)
condition = location.condition()

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    a=forecasts['high']
    b=forecasts['low']
    for i in a:
      print ([i])
      a=0
      if i>a:
        print(i)
        
