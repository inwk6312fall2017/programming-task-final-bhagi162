config=open("running-config.cfg")

for y in config:
  print(y)
  s = "172."
  for s in y:
    if s.isdigit():
        y.replace(s, "192.")
        print(y)
