from typing import List, NewType


class ListNode: 
    Data = ""    
    Pointer = -1
    def __init__(self,Data:str = "",Pointer:int = 0):
        self.Data = Data
        self.Pointer = Pointer
    def __str__(self):
        return(self.Data+" "+str(self.Pointer))

class LinkedList():
    CONST_NULLPOINTER = -1
    def __init__(self):
        self.List = []
        self.startPointer = self.CONST_NULLPOINTER
        self.freeListPointer = 0
        for i in range(4):
            self.List.append(ListNode(Pointer = i+1))
        self.List.append(ListNode(Pointer = self.CONST_NULLPOINTER)) 
    def print(self):
        for i in range(len(self.List)):
            print(self.List[i])
    def InsertNode(self,newItem):
        if self.freeListPointer != self.CONST_NULLPOINTER:
            self.newNodePointer = self.freeListPointer
            self.List[self.newNodePointer].Data = newItem  
            self.freeListPointer = self.List[self.freeListPointer].Pointer
            self.thisNodePointer = self.startPointer
            self.previousNodePointer = self.CONST_NULLPOINTER
            while self.thisNodePointer != self.CONST_NULLPOINTER and self.List[self.thisNodePointer].Data < newItem:
                self.previousNodePointer = self.thisNodePointer
                self.thisNodePointer = self.List[self.thisNodePointer].Pointer
            if self.previousNodePointer == self.CONST_NULLPOINTER:
                self.List[self.newNodePointer].Pointer = self.startPointer
                self.startPointer = self.newNodePointer
            else:
                self.List[self.newNodePointer].Pointer = self.List[self.previousNodePointer].Pointer
                self.List[self.previousNodePointer].Pointer = self.newNodePointer
    def FindNode(self,dataItem):
        self.currentNodePointer = self.startPointer
        while self.currentNodePointer != self.CONST_NULLPOINTER and self.List[self.currentNodePointer].Data != dataItem:
            self.currentNodePointer = self.List[self.currentNodePointer].Pointer
        return self.currentNodePointer
    def DeleteNode(self,dataItem):
        self.thisNodePointer = self.startPointer
        while self.thisNodePointer != self.CONST_NULLPOINTER and self.List[self.thisNodePointer].Data != dataItem:
            self.previousNodePointer =self.thisNodePointer
            self.thisNodePointer = self.List[self.thisNodePointer].Pointer
        if self.thisNodePointer != self.CONST_NULLPOINTER:
            if self.thisNodePointer == self.startPointer:
                self.startPointer = self.List[self.startPointer].Pointer
            else:
                self.List[self.previousNodePointer].Pointer = self.List[self.thisNodePointer].Pointer
            self.List[self.thisNodePointer].Pointer = self.freeListPointer
            self.freeListPointer = self.thisNodePointer
    def OutputAllNodes(self):
        self.currentNodePointer = self.startPointer# start at beginning of list
        if self.startPointer == self.CONST_NULLPOINTER:
            print("No data in list")
            print(self.currentNodePointer)
        while self.currentNodePointer != self.CONST_NULLPOINTER: # while not end of list
            print(self.currentNodePointer, "",self.List[self.currentNodePointer].Data)
            
            # follow the pointer to the next node
            self.currentNodePointer = List[self.currentNodePointer].Pointer



