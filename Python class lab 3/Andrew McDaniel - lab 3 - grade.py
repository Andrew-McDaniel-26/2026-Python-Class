# Andrew McDaniel, 10/1/26, this code will calculate your letter grade based of an inputed score
import math

# this line will output to the screen instructions for the user
x = int (input(" input you score out of 100 / "))

# this function will run through the if/else selections statments to determen the letter grade
def gradeScale(x):
 print(" your letter grade is")
 if x >= 90:
         print("A")
 else:
    if x < 90 and x >=  80: 
             print("B")
    else:
        if x  < 80 and x >= 70:
                print("c")
        else:
            if x < 70 and x >= 60: 
                 print("D")
            else:
                 if x < 60:
                  print("F")

gradeScale(x)