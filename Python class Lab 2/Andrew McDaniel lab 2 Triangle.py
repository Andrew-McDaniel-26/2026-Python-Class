import turtle
#Andrew McDaniel, Python Class Lab 2, 09/03/26, this program draws a triangle using turtle graphics

def drawTriangle(myTurtle, sideLength):
    myTurtle.color("red")
    myTurtle.begin_fill()
    for i in range(3):
        myTurtle.forward(sideLength)
        myTurtle.left(120)
    myTurtle.end_fill()
        # initialize the turtle and call the function to draw the triangle
t = turtle.Turtle()
drawTriangle(t, 100)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)