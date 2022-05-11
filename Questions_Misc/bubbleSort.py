data1 = [6,3,1,2,7,4,5]
data2 = [4,7,20,1,5,8,3,2,7]

def bubbleSort(data):
    for _ in range(len(data)):
        for curPNTR in range(1,len(data)):
            if data[curPNTR] < data[curPNTR-1]:
                data[curPNTR] , data[curPNTR-1] = data[curPNTR-1] , data[curPNTR]
                print(*data)


def InsertionSort(data):
    for i in range(1,len(data)):
        cmprPNTR = i - 1
        inserted = False
        while (cmprPNTR >= 0 and inserted == False):
            if(data[cmprPNTR + 1] < data[cmprPNTR]):
                data[cmprPNTR] , data[cmprPNTR + 1] = data[cmprPNTR + 1] , data[cmprPNTR]
                print(*data)
                cmprPNTR -= 1
            else:
                inserted = True

print("Bubble Sort")
bubbleSort(data1)
print("Insertion Sort")
InsertionSort(data2)