import time
dic1=dict()
dic2=dict()
def dictlist():
    f=open('dates.txt')
    for i in f:
        l=dic1.get(i,0)
        dic1[i]=l+1
        if dic1[i]>1:
            dic2[i]=dic1[i]
    print "dictionary is:",dic1
    return dic2
start=time.time()
finish=time.time()-start
print "filtered dictionary is",dictlist() 
