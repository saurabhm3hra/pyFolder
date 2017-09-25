import getopt
import sys


try:
        optlist, args = getopt.getopt(sys.argv[1:], "w:")
except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
if (len(optlist) < 1):
	print "Wrong Usage. Use -w <outfile> <infile1> <infile2> ..."
	sys.exit(2)
for o,a in optlist:
	if o == "-w":
		Outfile = a
	elif (len(args) < 1):
		print "Wrong Usage. Use -w <outfile> <infile1> <infile2> ..."
		sys.exit(2)
	else:
		print "Wrong Usage. Use -w <outfile> <infile1> <infile2> ..."
		sys.exit(2)
	
print Outfile
print args
