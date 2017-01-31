import string
# def alphabet_position(text):
#     returnedString = ""
#     for digit in enumerate(text):
#         if digit[1].isalpha() :
#             returnedString += str(string.ascii_lowercase.index(digit[1].lower()) + 1) + " "
#     returnedString = returnedString[:-1]
#     return returnedString

text = "the greatest 12'0 clock"
returnedString = ""
for digit in enumerate(text):
    if digit[1].isalpha() :
        returnedString += str(string.ascii_lowercase.index(digit[1].lower()) + 1) + " "
returnedString = returnedString[:-1]
print returnedString

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
