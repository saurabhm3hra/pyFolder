import turtle
import math
def square(t,l):
    for i in range(4):
        t.fd(l)
        t.lt(90)

def polygon(t,l,n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)

def circle(t,r,a):
    Circum = 2*math.pi*r
    l=Circum*a/360
    for i in range(int(360/a)):
        t.fd(l)
        t.lt(a)

bob = turtle.Turtle()
print(bob)
circle(bob,100,1)
turtle.mainloop()
