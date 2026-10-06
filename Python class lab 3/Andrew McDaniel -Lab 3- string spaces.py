# Andrew McDaniel, 10/6/26, python class
# this code will take an inputed string and remove the spaces
import string

b= input(" input here")

# the function the removes the strings
def stripSpace():
   # sets the total number of characters
    x = len(b)
    y = ""
    # the loop that checks every character
    for i in range(x):
        if b[i] != " ":
            y = y + b[i]
    # prints out the last blankspace
    return y

# prints the function
print(stripSpace())
