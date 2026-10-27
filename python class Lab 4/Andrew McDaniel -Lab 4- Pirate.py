# Andrew McDnaiel, Python class,  10/15 /26
# this program will chance your inputed sentace from english to pirate speak using strings and a dictonary


# the main function
def toPirate():
    # the dictonary for english to pirate
    pirateVocab = {"hello" : "avast", "sir" : "matey", "boy" :"matey" ,"man" : "matye", "woman" : "proud beauty" , "madam" : "proud beauty", "officer" : "foul blaggart" , "the" : "th'" , "my" : "me", "your" :"yer" , "is" : "be" , "are" : "be", "kitchen" : "gally" , "hotel" : "fleabag inn" }
    # the english sentace that is going to be translated
    englishStart = "hello there boy are you here at this hotel to enjoy the madam and her kitchen and it's famous food"

    # the loop that does the replacments of words in the string above
    for word, translation in pirateVocab.items():
        #replaces the english keys with pirate values
        englishStart = englishStart.replace(word, translation)
    print(englishStart)


toPirate()