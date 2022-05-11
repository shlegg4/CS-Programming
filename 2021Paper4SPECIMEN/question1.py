TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for Count in range(len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue] 
                NextValue = NextValue - 1 
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

def PrintARR(TheData):
    print("Contents of the data: ")
    for i in TheData:
        print(i)

print("Output before sorting :")
PrintARR(TheData)

InsertionSort(TheData)

print("Output after sorting :")
PrintARR(TheData)


def Find(TheData):
    numToFind = int(input("Please enter a number : "))
    if numToFind in TheData:
        print("Found")
        return True
    else:
        print("Not found")
        return False

Find(TheData)
Find(TheData)