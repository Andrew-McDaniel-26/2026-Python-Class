# Andrew McDaniel , python class , 10/13/26
# the goal of this program is to take the inputed sentence and count the number of words

#this will make your inputed senctace into a string
sentence = input("your sentence: ")

#this will split yout sentace into supstrings
words = sentence.split()

#this will count the number of substrings
wordCount = len(words)

# this will out put the nuber of substrings / words
print("number of words:", wordCount)