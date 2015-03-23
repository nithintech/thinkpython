class Time(object):
    print """Represent the time of the day.attributes:
             hour,minute,second"""
time=Time()
time.hour=int(raw_input("hour:"))
time.minute=int(raw_input("minute:"))
time.second=int(raw_input("seconds:"))
def repr_time():
    print "hour:minute:second"
    return '%.2d : %.2d : %.2d'%(time.hour,time.minute,time.second)

print repr_time()
