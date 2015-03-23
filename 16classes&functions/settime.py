class time(object):
    """represents the time of day.atributes:
       hour,minute,second"""

def timecheck(a,b):
    sec=(3600*a.h+60*a.m+a.s)-(3600*b.h+60*b.m+b.s)
    t=89999
    u=(t+sec)/t
    v=1-u
    d='true'
    e='false'
    print d*u+e*v

def main():
    p=time()
    q=time()
    p.h=int(raw_input("enter time one\nhour:"))
    p.m=int(raw_input("minute:"))
    p.s=int(raw_input("seconds:"))
    q.h=int(raw_input("enter time two\nhour:"))
    q.m=int(raw_input("minute:"))
    q.s=int(raw_input("seconds:"))
    timecheck(p,q)
main()
