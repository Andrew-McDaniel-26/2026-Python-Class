# Andrew McDaniel, Python calss, 10/15/26
# this program will create a dictonary of names and scores and then implement calculations and chances of and to that dictonaty
import math
# the two lists that get combinded
name = ["Joe", "Tom", "Barb", "Sue", "Sally"]
score = [10 , 23 , 13 , 18 , 12]

# the function that combines the two lists
def makeDictonary():
    makeDict = {}
    for i in range(len(name)):
        makeDict [name[i]] = score[i]
    return makeDict
#the main function
def scoreDict():
    #sets the dictonary to a new key to use so we don't change the original
    freshDict = makeDictonary()

#prints our the dictonary then prints out barb's score
    print(freshDict)
    print ("Barb's score is:",freshDict.get("Barb"))

#adds jhon and Jhon's score of 19, then prints the dict
    freshDict ["John"] = 19
    print(freshDict)

#sorts the list from the valus of each key then prints the sorted dictonary
    sortList = list (freshDict.values())
    sortList.sort()
    print(sortList)

# avrages the scores in the Dictonary and prints the average
    average =  (sum(sortList) / len(sortList))
    print("the average of the scores:",average)

# changes Sallys score to 13 then prints the Dictonary
    freshDict["Sally"] = 13
    print(freshDict)

# deletes Tom and his score from the dictonary then prints
    del freshDict ["Tom"]
    print(freshDict)


makeDictonary()
scoreDict()