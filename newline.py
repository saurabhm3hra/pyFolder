def newline(n):
	if n > 0:	
		print
		newline(n-1)

lines = int(raw_input("Input number of lines ->>>>>>>>>  "))
print "Hi, Whoever"
newline(lines)
