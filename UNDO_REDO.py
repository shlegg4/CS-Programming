from selectors import EpollSelector


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
            poppedITEM , self.STK[self.topPNTR] = self.STK[self.topPNTR] , -1
            if(abs(self.topPNTR - self.basePNTR) > 0):
                if(self.topPNTR > 0):
                    self.topPNTR -= 1
                else:
                    self.topPNTR = len(self.STK) - 1
            else:
                self.LimitReached = True
            return poppedITEM
        else:
            return None




class RedoUndo():
    def __init__(self):
       self.undoSTK = Stack(20)
       self.redoSTK = Stack(20)
       self.Str

    def undo(self):
        self.redoSTK.PUSH(self.undoSTK.POP())
    
    def redo(self):
        self.undoSTK.PUSH(self.redoSTK.POP())
    
    def append(self, item):

        
        

stk = RedoUndo()
for i in range(30):
    stk.PUSH(i)
stk.POP()
stk.POP()
stk.POP()
print(stk)