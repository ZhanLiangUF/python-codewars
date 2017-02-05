def pig_it(text):
    returnString = ""
    for word in text.split():
        returnString += word[1:] + word[:1]  + "ay" + " " if word.isalpha() else word + " "
    return returnString[0:-1]


# more optimized solution
#isalnum() returns true if all characters in the string are alphanumeric and there is at least one character
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
