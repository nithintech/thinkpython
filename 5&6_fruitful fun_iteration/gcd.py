a=int(raw_input("enter the numbers\n"))
b=int(raw_input())
def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  print a 
gcd(a,b)
