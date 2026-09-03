import turtle
#Andrew McDaniel, Python Class Lab 2, 09/03/26, this program draws a polygon using turtle graphics

#this is the function that draws the polygon
def drawPolygon(myTurtle, sideLength, numSides):
    myTurtle.color("blue")
    myTurtle.begin_fill()
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(360/numSides)
    myTurtle.end_fill()

# initialize the turtle and call the function to draw the polygon
t = turtle.Turtle()
drawPolygon(t, 2, 600)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)