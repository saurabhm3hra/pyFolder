import printf
series = {0:1, 1:1}
def fib(n):
	if(series.has_key(n)):
		return series[n]
	else:
		series[n] = fib(n-1) + fib(n-2)
		return series[n]

x = int(raw_input("Enter a number: --->"))
if x < 0:
	print "Input Correct No."
else:
	for i in range(0,x):
		printf.printf(str(fib(i)) + ",")

