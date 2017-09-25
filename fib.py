import printf
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
#		print "f(" + str(n-1) + ") + f(" + str(n-2) + ")" 
		return fib(n-1) + fib(n-2)

x = int(raw_input("Enter a number: --->"))
if x < 0:
	print "Input Correct No."
else:
	for i in range(0,x):
		printf.printf(str(fib(i)) + ",")

