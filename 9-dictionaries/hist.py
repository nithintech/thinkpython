s=str(raw_input())
def hist(s):
    dic=dict()
    for i in s:
        s=dic.get(i,0)
        dic[i]=s+1
    #print dic
    for k,v in dic.items():
        print k,v
hist(s)
