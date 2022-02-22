class Node:
    def __init__(self,nextPNTR,prePNTR,PNTR,item):
        self._item = item
        self._nextPNTR = nextPNTR
        self._prePNTR = prePNTR
        self._PNTR = PNTR

class LinkedList:
    def __init__(self):
        self._list = []
        self._curPNTR = 0
    
    def Append(self,value,PNTR):
        try:
            preNode = self._list[-1]
            nextNode = Node(None,preNode._PNTR,PNTR,value)
            self._list[-1]._nextPNTR = PNTR
            self._list.append(nextNode)
            self._curPNTR = PNTR
        except IndexError:
            nextNode = Node(None,0,value)
            self._list.append(nextNode)
        except:
            raise Exception("Unknow error occured")

    def Remove(self,):