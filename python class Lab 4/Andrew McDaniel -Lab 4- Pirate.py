# Andrew McDnaiel, Python class,  10/15 /26
# this program will chance your inputed sentace from english to pirate speak using strings and a dictonary



def toPirate():
    pirateVocab = {"hello" : "avast", "sir" : "matey", "boy" :"matey" ,"man" : "matye", "woman" : "proud beauty" , "madam" : "proud beauty", "officer" : "foul blaggart" , "the" : "th'" , "my" : "me", "your" :"yer" , "is" : "be" , "are" : "be", "kitchen" : "gally" , "hotel" : "fleabag inn" }
    englishStart = "hello there boy are you here at this hotel to enjoy the madam and her kitchen and it's famous food"

    
    for word, translation in pirateVocab.items():
        englishStart = englishStart.replace(word, translation)
    print(englishStart)


toPirate()