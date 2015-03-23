print "enter 2numbers"
a=int(raw_input())
b=int(raw_input())
def power(a,b):
  p=a%b
  q=(a/b)%b
  if p==0:
    if q==0:
      return True
  else:
    return False  
print power(a,b)
