# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that 
# contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    dictionary = {}
    if string is "": return True
    for c in string:
        if not c.lower() in dictionary:
            dictionary[c] = 1
        else:
            return False
    return True
