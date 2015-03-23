strng="qwer tttr rest trew kks qwe fde"
word=strng.split(" ")
lis1=[]
lis2=[]
new=[]
def lensort(words):
    for each in words:
       lis1.append((len(each),each))
    lis2=sorted(lis1,reverse=True)
    #print lis2
    for i in lis2:
        new.append(i[1])
    print new
lensort(word)
