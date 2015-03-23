class Time(object):
   """add seconds"""
def increment(time,sec):
    time.second+=sec
    if time.second>=60:        
        minute=time.second/60
        time.minute+=minute
    if time.minute>=60:
        hour=time.minute/60
        time.hour=(hour+time.hour)%24
        time.minute=time.minute%60
    time.second=time.second%60
    print "after adding\n",time.hour,':',time.minute,':',time.second
time=Time()
sec=int(raw_input("seconds:"))
time.hour=5
time.minute=30
time.second=40
print "time before adding\n",time.hour,':',time.minute,':',time.second
increment(time,sec)
