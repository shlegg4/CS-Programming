import Constants as C

class TreeNode():
    leftPointer = 0
    rightPointer = 0 
    data = ""
    def __init__(self,LeftPointer=0,RightPointer=0,Data = ""):
        self.data = Data
        self.leftPointer = LeftPointer
        self.rightPointer = RightPointer


class BinaryTree():
    
    rootPointer = 0
    freePointer = 0
    def __init__(self):
        self.tree  = [TreeNode() for i in range(7)]
        self.rootPointer = C.nullPointer
        self.freePointer = 0
        for i in range(6):
            self.tree[i].leftPointer = i+1
        self.tree[6].leftPointer = C.nullPointer
    def InsertNode(self,newItem):
        if self.freePointer != C.nullPointer:
            self.newNodePointer = self.freePointer
            self.freePointer = self.tree[self.freePointer].leftPointer
            self.tree[self.newNodePointer].data = newItem
            self.tree[self.newNodePointer].leftPointer = C.nullPointer
            self.tree[self.newNodePointer].rightPointer = C.nullPointer
            if self.rootPointer == C.nullPointer:
                self.rootPointer = self.newNodePointer
            else:
                self.thisNodePointer = self.rootPointer
                while self.thisNodePointer != C.nullPointer:
                    self.previousNodePointer  = self.thisNodePointer
                    if self.tree[self.thisNodePointer].data > newItem:
                        self.TurnedLeft = True
                        self.thisNodePointer = self.tree[self.thisNodePointer].leftPointer
                    else:
                        self.TurnedLeft = False
                        self.thisNodePointer = self.tree[self.thisNodePointer].rightPointer
                if self.TurnedLeft == True:
                    self.tree[self.previousNodePointer].leftPointer = self.newNodePointer
                else:
                    self.tree[self.previousNodePointer].rightPointer = self.newNodePointer
    def FindNode(self,searchItem):
        self.thisNodePointer = self.rootPointer
        while self.thisNodePointer != C.nullPointer and self.tree[self.thisNodePointer].data != searchItem:
            if self.tree[self.thisNodePointer].data > searchItem:
                self.thisNodePointer = self.tree[self.thisNodePointer].leftPointer
            else:
                self.thisNodePointer = self.tree[self.thisNodePointer].rightPointer
        return self.thisNodePointer


SamsTree = BinaryTree()
SamsTree.InsertNode("F")
SamsTree.InsertNode("C")
SamsTree.InsertNode("S")
SamsTree.InsertNode("B")
SamsTree.InsertNode("E")
SamsTree.InsertNode("R")
SamsTree.InsertNode("D")
print(SamsTree.FindNode("F"))
print(SamsTree.FindNode("D"))
