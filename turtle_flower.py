import turtle
import math
def circle(t,r,a):
    Circum = (2*math.pi*r)
    l=Circum*a/360
    for i in range(4):
        for i in range(2):
            for j in range(int(360/(a*4))):
                t.fd(l)
                t.lt(a)
            t.lt(360/(a*4))
        t.lt(360/(a*4))

bob1 = turtle.Turtle()
print(bob1)
circle(bob1,100,1)
turtle.mainloop()
