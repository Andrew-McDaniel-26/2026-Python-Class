import turtle
#Andrew McDaniel, Python Class Lab 2, 09/03/26, this
def drawSpiral(myTurtle, maxsides):
    myTurtle.color("blue")
    for sidelength in range(1, maxsides+1, 5):
        myTurtle.forward(sidelength)
        myTurtle.right(90)

# initialize the turtle and call the function to draw the spiral
t = turtle.Turtle()
drawSpiral(t, 100)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)