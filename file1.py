f = open("s.txt","w")
f.write("Hello World!\n")
f.write("ok")
f.close()

f = open("s.txt", "r")
print f.read()
f.close()
