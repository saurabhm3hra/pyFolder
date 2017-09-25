f1 = open("s.txt","r")
f2 = open("s2.txt","w")
while True:
	text = f1.readline()
	if text == "":
		break
	else:
		f2.write(text)

f1.close()
f2.close()
