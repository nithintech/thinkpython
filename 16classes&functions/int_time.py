class Time(object):
    def seconds(sec):
        t=(sec.h*3600)+(sec.m*60)+(sec.s)
        return t

time=Time()
time.h=int(raw_input("enter time\nhours:"))
time.m=int(raw_input("minutes:"))
time.s=int(raw_input("seconds:"))
print time.seconds()

