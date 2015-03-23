print "enter three sides of triangle"
x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
def istriangle(x,y,z):
  if (x+y)>=z and (y+z)>=x and (z+x)>=y:
    print "yes"
  else:
    print "no"
istriangle(x,y,z)

