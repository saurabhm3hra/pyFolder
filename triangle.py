space=int(raw_input("Length of Side ---> ")) - 1
middle=0
while space >= 0:
	if space==0:
		print " "*space + "/" + "_"*middle + "\\" + " "*space
		break
	else:
		print " "*space + "/" + " "*middle + "\\" + " "*space
		space = space - 1
		middle = middle + 2
