#python UNDO_REDO.py


redoSTK = []
undoSTK = []
string = ["" for _ in range(50)]

class Stack:
    def __init__(self,len):
        self.STK = [(0,0) for _ in range(len)]
        self.length = len
        self.basePNTR = 0
        self.topPNTR = 0
        self.LimitReached = False

    def Clear(self):
        for i in range(self.length):
            self.STK[i] = (0,0)
    def PUSH(self,item):
        self.LimitReached = False
        self.STK[self.topPNTR] = item

        if(self.topPNTR < len(self.STK)):
            self.topPNTR += 1
        else:
            self.topPNTR = 0
        
        if(self.topPNTR == self.basePNTR):
            self.basePNTR += 1
    
    def POP(self):
        if not(self.LimitReached):
            if(abs(self.topPNTR - self.basePNTR) > 0):
                if(self.topPNTR > 0):
                    self.topPNTR -= 1
                else:
                    self.topPNTR = len(self.STK) - 1
            else:
                self.LimitReached = True
                return
            poppedITEM , self.STK[self.topPNTR] = self.STK[self.topPNTR] , -1
            return poppedITEM
        else:
            return 




class RedoUndo():
    def __init__(self):
       self.undoSTK = Stack(20)
       self.redoSTK = Stack(20)
       self.line = []

    def undo(self):
        try:
            self.redoSTK.PUSH(self.undoSTK.POP())
            self.line.pop()
        except IndexError:
            print("Nothing left to undo.")
    
    def redo(self):
        item = self.redoSTK.POP()
        if(item != None):
            self.line.append(item)
            self.undoSTK.PUSH(item)

    def append(self, item):
        self.line.append(item)
        self.undoSTK.PUSH(item)
        self.redoSTK.Clear()
        
def Main():
    undoHandler = RedoUndo()
    while True:
        choice = input("A:append,U:undo,R:redo, followed by letter:\n")
        if("A" in choice):
            item = choice.replace("A:", "")
            undoHandler.append(item)
        elif("U" in choice):
            undoHandler.undo()
        elif("R" in choice):
            undoHandler.redo()
        print(undoHandler.line)

Main()