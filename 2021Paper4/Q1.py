TheData = [20,3,4,8,12,99,4,26,4]


#Terrible version from test
def InsertionSortBad(data):
    for count in range(1, len(data)):
        dataToInsert = data[count]
        inserted = 0
        nextValue = count -1
        while (nextValue >= 0 and inserted != 1):
            if (dataToInsert < data[nextValue]):
                data[nextValue + 1] = data[nextValue]
                nextValue -= 1
                data[nextValue + 1] = dataToInsert
            else:
                inserted = 1
    return data


#My version 
def InsertionSort():
    global TheData
    for i in range(1,len(TheData)):
        cmprPNTR = i - 1
        inserted = False
        while (cmprPNTR >= 0 and inserted == False):
            if(TheData[cmprPNTR + 1] < TheData[cmprPNTR]):
                TheData[cmprPNTR] , TheData[cmprPNTR + 1] = TheData[cmprPNTR + 1] , TheData[cmprPNTR]
                cmprPNTR -= 1
            else:
                inserted = True


def PrintArray():
    global TheData
    for element in TheData:
        print(element,end = " ")
    print()

def InArray():
    global TheData
    checkVal = int(input("Please input number :"))
    if checkVal in TheData:
        print("Found")
        return True
    else:
        print("Not found")
        return False




print("Before sorting:")
PrintArray()
InsertionSort()
print("After sorting:")
PrintArray()
InArray()


