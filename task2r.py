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
    
    print(a,b)
    
    list1=[a]
    list2=[b]
    
    
    print ("Max value element : ", max(list1))
    print ("Max value element : ", max(list2))
