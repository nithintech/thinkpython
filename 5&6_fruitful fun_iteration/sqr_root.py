#newton's square root method

num=int(raw_input("enter number:"))
def sqr_root(num):
  x=3.0
  while True:
    y=(x+num/x)/2
    if y==x:
      break
    x=y
  print x
sqr_root(num)
