x=str(raw_input("enter the string"))
def palindrome(x):
  while(x):
    if x=='':
      return "palindrome"
    else: 
      if x[0]==x[-1]:
        palindrome(x[1:-1])
print palindrome(x)
