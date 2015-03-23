print "enter x and y to compare"
x=int(raw_input())
y=int(raw_input())
def comp(x,y):
  if x>y:
     return 1
  elif x==y:
    return 0
  elif x<y:
    return -1
print comp(x,y)
