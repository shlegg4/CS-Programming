QueueData = [0 for _ in range(20)]
nullPNTR  = -1
startPNTR = 0 
endPNTR = 19
freePNTR = startPNTR

def Enqueue(item):
    global freePNTR, QueueData

    if freePNTR < endPNTR and freePNTR != nullPNTR:
        QueueData[freePNTR] = item
        if freePNTR + 1 == endPNTR:
            freePNTR = nullPNTR
        else:
            freePNTR += 1
        return True
    else:
        return False

def ReadFile():
    fileName = input("User please enter a file name : ")
    try:
        with open(fileName, "r") as f:
            for i,line in enumerate(f):
                if i <= endPNTR:
                    QueueData[i] = line.strip()
                else:
                    return 1
        return 2
    except FileNotFoundError:
        return -1

state = ReadFile()
if state == 2:
    print("All items were added to the queue")
elif state == 1:
    print("The queue was full")
elif state == -1:
    print("The text file could not be found")

def Remove():
    global startPNTR
    if not startPNTR + 2 > endPNTR:
        concatenated = f"{QueueData[startPNTR]} {QueueData[startPNTR+1]}"
        QueueData[startPNTR], QueueData[startPNTR+1] = 0, 0
        startPNTR += 2
        return concatenated
    else:
        return "No Items"

print(Remove())