import turtle
#Andrew McDaniel, Python Class Lab 2, 09/01/26, this program draws a star using turtle graphics

#this is the function that draws the star
def drawstar(myTurtle, sideLength):
    myTurtle.color("blue")
    for i in range(5):
        myTurtle.forward(sideLength)
        myTurtle.right(144)

# initialize the turtle and call the function to draw the star
t = turtle.Turtle()
drawstar(t, 100)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)