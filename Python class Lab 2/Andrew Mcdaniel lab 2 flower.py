

import turtle 
#Andrew McDaniel, Python Class Lab 2, 09/01/26, this program draws a flower with a stem using turtle graphics

#this is the function that draws the flower and stem
def drawflower(myTurtle, petalLength, stemLength):
	# sets the color of the flower petals to green and the fill color to blue
	myTurtle.color("green", "blue")
	# draws 6 flower petals
	for i in range(6):
		myTurtle.begin_fill()
		myTurtle.circle(petalLength, 60)
		myTurtle.left(120)
		myTurtle.circle(petalLength, 60)
		myTurtle.end_fill()
		myTurtle.left(60)
	#draws the stem
	myTurtle.right(54)
	myTurtle.forward(stemLength)

# initialize the turtle and call the function to draw the flower
t = turtle.Turtle()
drawflower(t, 50, 100)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)