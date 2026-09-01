import turtle

def drawstar(myTurtle, sideLength):
    myTurtle.color("blue")
    for i in range(5):
        myTurtle.forward(sideLength)
        myTurtle.right(144)

t = turtle.Turtle()
drawstar(t, 100)