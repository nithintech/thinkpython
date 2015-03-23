import math
class dist():
  print "distance b/w points"
a=dist()
b=dist()
a.x=int(raw_input("enter x cordinates\n"))
b.x=int(raw_input())
a.y=int(raw_input("y cordinates\n"))
b.y=int(raw_input())
def distance():
  m=a.x-b.x
  n=a.y-b.y
  d=math.sqrt(m**2+n**2)
  return d
print distance()
