# Andrew McDaniel, Python calss, 10/15/26
# this program will create a dictonary of names and scores and then implement calculations and chances of and to that dictonaty
import math

name = ["Joe", "Tom", "Barb", "Sue", "Sally"]
score = [10 , 23 , 13 , 18 , 12]

def makeDictonary():
    makeDict = {}
    for i in range(len(name)):
        makeDict [name[i]] = score[i]
    return makeDict

def scoreDict():
    freshDict = makeDictonary()

    print(freshDict)
    print ("Barb's score is:",freshDict.get("Barb"))

    freshDict ["John"] = 19
    print(freshDict)

    sortList = list (freshDict.values())
    sortList.sort()
    print(sortList)

    average =  (sum(sortList) / len(sortList))
    print("the average of the scores:",average)

    freshDict["Sally"] = 13
    print(freshDict)

    del freshDict ["Tom"]
    print(freshDict)

makeDictonary()
scoreDict()