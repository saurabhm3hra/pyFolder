import math
class point:
	pass

def print_point(pt):
	print pt.x, pt.y

def dist(pt1,pt2):
	distance = math.sqrt((float(pt1.x) - float(pt2.x))**2 + (float(pt1.y) - float(pt2.y))**2)
	return distance

point1 = raw_input("Enter Point 1: (x,y)")
point2 = raw_input("Enter Point 2: (x,y)")
x1 = point1.split(',')[0]
y1 = point1.split(',')[1]
x2 = point2.split(',')[0]
y2 = point2.split(',')[1]

pt1 = point()
pt2 = point()
pt1.x = x1
pt1.y = y1
pt2.x = x2
pt2.y = y2

print_point(pt1)
print_point(pt2)
print "Distance between the points is %.2f" % dist(pt1,pt2)
