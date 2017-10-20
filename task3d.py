y=[]
config=open("running-config.cfg")
for line in config:
  b=line.split()
  

  
  for n,i in enumerate(b):
   if i== 172:
     b[n]=192
     print(b[n])
