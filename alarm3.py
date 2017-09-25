#! /usr/bin/env python3

import string
import re
import os
import sys
import getopt


Outfile = ""

try:
        optlist, args = getopt.getopt(sys.argv[1:], "w:")
except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
if (len(optlist) < 1):
        print("Wrong Usage. Use -w <outfile> <infile1> <infile2> ...")
        sys.exit(2)
for o, a in optlist:
        if o == "-w":
                Outfile = a
        elif (len(args) < 1):
                print("Wrong Usage. Use -w <outfile> <infile1> <infile2> ...")
                sys.exit(2)
        else:
                print("Wrong Usage. Use -w <outfile> <infile1> <infile2> ...")
                sys.exit(2)

out = []
out.append(",HIST,NE,UNIT,TYPE,DATE,SEVERITY,TYPE2,TUNIT,LOC,PRB,ALM_No,ALARM,ADD_INFO\n")

for i in range(0, len(args)):
	f = open(args[i], "rU")
	while True:
		s = f.readline()
		if s.startswith("    <HIST>"):
			temp = []
			temp.append(s[0:11])
			temp.append(s[11:34])
			temp.append(s[34:46])
			temp.append(s[46:56])
			temp.append(s[56:-1])
			out.append(", ".join(temp))
			for i in range(0, 3):
				s = f.readline()
				if i == 0:
					temp = []
					temp.append(s[0:4])
					temp.append(s[4:11])
					temp.append(s[11:23])
					temp.append(s[23:45])
					temp.append(s[45:-1])
					out.append(", ".join(temp))
				elif i == 1:
					temp = []
					temp.append(s[5:9])
					temp.append(s[11:-1])
					out.append(", ".join(temp))
				else:
					out.append(s)
		if s == '':
			break
	f.close()
f2 = open(Outfile, "w")
f2.write(", ".join(out))
f2.close()
