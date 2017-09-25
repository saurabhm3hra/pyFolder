import math
import time
time1 = time.time()
days = time1/(60*60*24)
hours = 24*(days - int(days))
minutes = (24*60*(days - int(days)))%60
seconds = (24*60*60*(days - int(days)))%60
print "Days Since Epoch:", int(days)

date=1
year=1970
month=1
for i in range(int(days)):
    if(year%4==0):
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            if(date==31):
                date=0
                month=month+1
        if(month==2):
            if(date==29):
                date=0
                month=month+1
        if(month==4 or month==6 or month==9 or month==11):
            if(date==30):
                date=0
                month=month+1
        if(month==12):
            if(date==31):
                date=0
                month=1
                year=year+1
    else:
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
            if(date==31):
                date=0
                month=month+1
        if(month==2):
            if(date==28):
                date=0
                month=month+1
        if(month==4 or month==6 or month==9 or month==11):
            if(date==30):
                date=0
                month=month+1
        if(month==12):
            if(date==31):
                date=0
                month=1
                year=year+1
    date=date+1

print "[Time hh:mm:ss | dd/mm/yyyy]",int(hours),":",int(minutes),":",int(seconds)," | ",date,"/",month,"/",year
#print int(minutes)
#print int(seconds)
#print date
#print month
#print year
