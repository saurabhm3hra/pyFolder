import math

def Log(x,y):
	if(x<0 or y <0):
		print "Negative values not accepted"
		return
	else:
		z = math.log(x,y)
		return z

x = int(raw_input("Enter value: "))
y = int(raw_input("Enter Base: "))
i=1
while i <= x:
	print "Log("+str(i)+ ","+str(y)+")"+'\t'+str(math.log(i,y))
	i=i+1
