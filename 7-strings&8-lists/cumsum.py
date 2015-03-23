lim=int(raw_input("enter lim:\n"))
print "enter list:"
x=[int(raw_input()) for x in range(lim)]
print "the list input is",x
y=[]
def cum(x):
	k=0
	for i in x:
		k=i+k
		y.append(k)
	print y
cum(x)
	
