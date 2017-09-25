import os
import shelve

sh = shelve.open('mydata')
for i in list(sh.keys()):
	print(type(i))
	print(sh[i])
sh.close()
