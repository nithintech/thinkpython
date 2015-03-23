t=tuple()
lis1=[]
dic=dict()
w=open("word.txt")
def freq_let():
    for i in w:
        i=i.strip()
        s=i
        for j in s:
            k=dic.get(j,0)
            dic[j]=k+1
    new=dic.items()
    #print new
    lis1=sorted(new,key=lambda x:x[1],reverse=True)
    #print lis1
    for m in lis1:
        if m[0]==" " or m[0]=="'" or m[0]=="." or m[0]==";"or m[0]=="," :
            del m
        else:
            print m[0],"   ",m[1]
    
freq_let() 
