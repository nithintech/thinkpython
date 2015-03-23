print "enter x y z"
x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
def isbetween(x,y,z):
  if x<=y:
    if y<=z:
      print "true"
  else:
    print "false"
isbetween(x,y,z)
