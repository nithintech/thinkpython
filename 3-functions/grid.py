def first(n): #i =no.of times
  a='+'
  b='-'
  print ((a+b*4)*2+a)
def second(n): #j=no.of times
  c='|'
  d=' '
  print ((c+d*4)*2+c)
def drawg(n):
  first(n)
  while n>0:
    second(n)
    second(n)
    first(n)
    n=n-1
drawg(4)
