class point:
	def __init__(self,x=0,y=0):
		self.x = float(x)
		self.y = float(y)

	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"

p = point(3,5)
print p
