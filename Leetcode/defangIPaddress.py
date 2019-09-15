def validateIpAddress(ipAddr):
    numPeriod = 0
    for i in ipAddr:
        if (i=='.'):
            numPeriod+=1
    #print ("Number of Periods : ",numPeriod)
    if (numPeriod == 3):
        pass
    else :
        return ("0")
    ipAddrSplit = ipAddr.split('.')
    for j in ipAddrSplit:
        if (j.isdigit()):
            if (int(j)>=0 and int(j)<=255):
                pass
            else:
                return ("0")
        else:
            return ("0")
    return ("1")

def defangIpAddress():
    ipAddr = input("Enter IP address : ")
    #print (ipAddr)
    if (validateIpAddress(ipAddr)=='1'):
        defangIpAddr = ipAddr.replace('.','[.]')
        return (defangIpAddr)
    else :
        return ("Invalid IP Address")

print (defangIpAddress())
