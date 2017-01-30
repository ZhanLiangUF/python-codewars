import string
def alphabet_position(text):
    returnedString = ""
    for digit in enumerate(text):
        if digit[1].isalpha() :
            returnedString += str(string.ascii_lowercase.index(digit[1].lower()) + 1) + " "
    returnedString = returnedString[:-1]
    return returnedString
