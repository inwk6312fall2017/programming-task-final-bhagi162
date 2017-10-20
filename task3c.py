import re

config=open("running-config.cfg")
for y in config:
  print(y)
  
  s=re.sub("\d", "172", "192")
  print(s)
