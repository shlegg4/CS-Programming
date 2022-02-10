import readline


QueueData = ["" for _ in range(20)]
startPNTR = 0
endPNTR = 19

def Enqueue(item):
    global startPNTR, QueueData
    if startPNTR <= endPNTR:
        QueueData[startPNTR] = item
        startPNTR += 1
        return True
    else:
        return False
    
def ReadFile():
    global startPNTR,endPNTR
    fileDirectory = input("Please enter your file directory : ")
    try:
        with open(fileDirectory, "r") as file:
            room = True
            while room:
                data = file.readline()
                if "" != data: 
                    room = Enqueue(data)
                else:
                    room = False
        if startPNTR <= endPNTR:
            return 2
        else:
            return 1
    except:
        return -1

def Remove():
    




result = ReadFile()
if result == -1:
    print("The text file could not be found")
elif result == 1:
    print("Not all data from file could be loaded into queue")
elif result == 2:
    print("All items were loaded successfully into queue")

print(*QueueData)