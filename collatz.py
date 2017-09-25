def collatz(x):
	while x != 1:
		if x % 2 == 0:
			x = x // 2
			print(str(x))
		else:
			x = x * 3 + 1
			print(str(x))


x = 111111
collatz(x)
