a=int(raw_input("enter two numbers\n"))
b=int(raw_input())
def gcd(a,b):
  if a>b:
    if (a%b)==0:
      return b
    else:
      return gcd(b,a%b)
  elif b>a:
    if (b%a)==0:
      return a
    else:
      return gcd(a,b%a)
print gcd(a,b)
