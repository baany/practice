def validateLength(stones, jewels):
    lengthStone = len(stones)
    lengthJewel = len(jewels)
    if (lengthStone <= 50 and lengthJewel <= 50):
        return ([1,1])
    else:
        return ("Length of stone and jewel list should be <= 50")

def uniqueJewelString(jewels):
    if len(set(jewels))==len(jewels):
        return (1)
    else:
        return (0)

def numberofJewelsinStones():
    stones = input("Enter the stone string : ")
    jewels = input("Enter the jewel string : ")
    validationList = validateLength(stones, jewels)
    jewelValidateChar = uniqueJewelString(jewels)
    if (validationList[0]==1 and validationList[1]==1 and jewelValidateChar==1):
        #print ("Jewels and Stones lists are valid")
        pass
    elif (jewelValidateChar==0):
        print ("Jewels list has non-unique characters")
    else :
        print (validationList)
    jewelCount = 0
    for j in list(stones):
        if (j in list(jewels)):
            jewelCount +=1
        else :
            pass                
    return (jewelCount)

print (numberofJewelsinStones())
