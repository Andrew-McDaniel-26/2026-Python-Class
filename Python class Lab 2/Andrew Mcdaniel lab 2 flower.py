

import turtle 
#Andrew McDaniel, Python Class Lab 2, 09/03/26, this program draws a flower with a stem using turtle graphics

#this is the function that draws the flower and stem
def drawflower(myTurtle, petalLength, stemLength):
	myTurtle.color("green", "blue")
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.left(60)
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.left(60)
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.left(60)
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.left(60)
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.left(60)
	myTurtle.begin_fill()
	myTurtle.circle(petalLength, 60)
	myTurtle.left(120)
	myTurtle.circle(petalLength, 60)
	myTurtle.end_fill()
	myTurtle.right(54)
	myTurtle.forward(stemLength)

# initialize the turtle and call the function to draw the flower
t = turtle.Turtle()
drawflower(t, 50, 100)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)