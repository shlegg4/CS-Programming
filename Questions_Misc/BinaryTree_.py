from logging import root
from re import A


class node:
    def __init__(self,val = None, leftPNTR = -1, rightPNTR = -1):
        self._val = val
        self._leftPNTR = leftPNTR
        self._rightPNTR = rightPNTR

arrayNodes = [node() for _ in range(20)]
rootPointer = -1
freePointer = 0

def addNode(arrayNodes, rootPointer, freePointer):
    nodeData = int(input("Please enter a number :"))
    if freePointer <= 19:
        arrayNodes[freePointer]._leftPNTR = -1
        arrayNodes[freePointer]._rightPNTR = -1
        arrayNodes[freePointer]._val = nodeData
        if rootPointer == -1:
            rootPointer = 0
        else:
            placed = False
            curPointer = rootPointer
            while not placed:
                if nodeData < arrayNodes[curPointer]._val:
                    if arrayNodes[curPointer]._leftPNTR == -1:
                        arrayNodes[curPointer]._leftPNTR = freePointer
                        placed = True
                    else:
                        curPointer = arrayNodes[curPointer]._leftPNTR
                else:
                    if arrayNodes[curPointer]._rightPNTR == -1:
                        arrayNodes[curPointer]._rightPNTR = freePointer
                        placed = True
                    else:
                        curPointer = arrayNodes[curPointer]._rightPNTR
        freePointer += 1
    else:
        print("Tree is full")
    return arrayNodes, rootPointer, freePointer
    

def PrintAll(arrayNodes):
    for node in arrayNodes:
        print(f"{node._leftPNTR}    {node._val}     {node._rightPNTR}")


def inOrder(arrayNodes, rootPointer):
    if arrayNodes[rootPointer]._leftPNTR != -1:
        inOrder(arrayNodes, arrayNodes[rootPointer]._leftPNTR)
    print(arrayNodes[rootPointer]._val)
    if arrayNodes[rootPointer]._rightPNTR != -1:
        inOrder(arrayNodes, arrayNodes[rootPointer]._rightPNTR)


rootPointer = -1
freePointer = 0

for i in range(10):
   arrayNodes, rootPointer, freePointer = addNode(arrayNodes, rootPointer, freePointer)
print("In row order ->\nLeftPointer     Data    RightPointer\n")
PrintAll(arrayNodes)
print("In value order ->\n")
inOrder(arrayNodes, rootPointer)