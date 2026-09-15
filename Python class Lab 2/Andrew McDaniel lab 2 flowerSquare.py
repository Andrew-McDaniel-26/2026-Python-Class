import turtle

def drawsSqare(myTurtle, sideLength,numSides):
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def drawFlower(myTurtle, drawsSqare, sideLength, numSides):
    myTurtle.color("green", "blue")
    for i in range(36):
        turtle.begin_fill()
        drawsSqare(myTurtle, sideLength, numSides)
        turtle.end_fill() 
        myTurtle.right(10)
        
    myTurtle.right(90)
    myTurtle.forward(100)


t = turtle.Turtle()
drawFlower(t, drawsSqare, 25,4)

# this is to keep the turtle graphics window open until the user closes it
x = ""
input(x)
print(x)