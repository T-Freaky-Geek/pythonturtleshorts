from turtle import *

t=Turtle()

bgcolor("#556677")
t.ht()
t.speed(0)

for i in range(360*2):
	t.goto(0,0)
	t.right(0.5)
	t.fd(250)

done()