def openOrSenior(data):
    returnList = []
    for i,j in data:
        if i >= 55 and j > 7:
            returnList.append("Senior")
        else:
            returnList.append("Open")
    return returnList
