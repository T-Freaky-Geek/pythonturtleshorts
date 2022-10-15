from turtle import *

t=Turtle()

bgcolor("#556677")
t.ht()
t.speed(0)

def square(side):
	for i in range(4):
		t.fd(side)
		t.right(90)

for i in range(360):
	t.goto(0,0)
	t.fd(100)
	t.right(1)
	square(30)

done()