print "enter the string"
x=str(raw_input())
new=x.lower()
new=new[::-1]
print new
if x==new:
  print "palindrome"
else:
  print "no"
