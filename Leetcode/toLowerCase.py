def toLowerCase(stringVal):
    lstr = ""
    for i in stringVal:
        if (ord(i)>=65 and ord(i)<=91):
            lstr += chr(ord(i)+32)
        else:
            lstr += i
    return (lstr)

print (toLowerCase("Al$%^PhABEt"))

