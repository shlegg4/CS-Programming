import imp
import sys
import linecache


class interpreter:
    def __init__(self,dir,memoryBlockSize = 200):
        self._instructionSet = {"LDM":self.LDM,"LDD":self.LDD,"LDI":self.LDI,"LDX":self.LDX,"LDR":self.LDR,"MOV":self.MOV,"STO":self.STO,"STX":self.STX,"STI":self.STI,"ADD":self.ADD,"SUB":self.SUB,"INC":self.INC,"DEC":self.DEC,  "END":self.END}
        self._ACC = 0
        self._IX = 0
        self._JMPFlag = False
        self._memory = [0 for _ in range(memoryBlockSize)]
        self._symbolicAddress = {}
        self._dir = dir

    def Run(self):
        EOF = False
        self._linePNTR = 0 
        while EOF == False:
            self._linePNTR += 1
            line = linecache.getline(self._dir,self._linePNTR)
            
            infixLine = []
            lexemes = line.split(" ")
            for lexeme in lexemes:
                try:
                    infixLine.append(self._instructionSet[lexeme.replace("\n","")])
                except KeyError as error:
                    print(error)
                    try:
                        infixLine.append(self._symbolicAddress[lexeme.replace("\n","")])
                    except:
                        if "#" in lexeme:
                            infixLine.append(int(lexeme.replace("#","")))
                        elif "@" in lexeme:
                            infixLine.append(int(lexeme.replace("@","")))
                        else:
                            print("Invalid syntax: {0} on line {1}".format(lexeme, linePNTR))
                            self.END()

            try:
                lexeme[0](lexeme[1])
            except:
                lexeme[0]()

    def LDM(self, number : int):
        self._ACC = number
    
    def LDD(self,address):
        try:
            self._ACC = self._memory[address]
        except:
            print("Object does not exist in memory")
            sys.exit()
    
    def LDI(self,address):
        try:
            self._ACC = self._memory[self._memory[address]]
        except:
            print("Object does not exist in memory")
    
    def LDX(self, address):
        try:
            address = self._memory[address]
            self._ACC = self._memory[address + self._IX]
        except:
            print("Object does not exist in memory")

    def LDR(self,number : int):
        self._IX = number

    def MOV(self):
        self._IX = self._ACC

    def STO(self, address):
        try:
            self._memory[address] = self._ACC
        except:
            print("Address too large for memory")

    def STX(self,address):
        try:
            self._memory[address + self._IX] = self._ACC
        except:
            print("Address too large for memory")
        
    def STI(self,address):
        try:
            self._memory[self._memory[address]] = self._ACC
        except:
            print("Address too large for memory")
    
    def ADD(self,operand):  #Add and sub wont work because it will always default to the memory address 
        try:
            self._ACC += self._memory[operand]
        except:
            try:
                self._ACC += operand
            except:
                print("ERROR")
    
    def SUB(self, operand):
        try:
            self._ACC -= self._memory[operand]
        except:
            try:
                self._ACC -= operand
            except:
                print("ERROR")
    
    def INC(self):
        self._ACC += 1
    
    def DEC(self):
        self._ACC -= 1
    
    def JMP(self,address):
        self._linePntr = address
    
    def CMP(self,operand):
        try:
            self._JMPFlag = self._ACC == self._memory(operand)
        except:
            try:
                self._JMPFlag = self._ACC == operand
            except:
                print("ERROR")
    
    def CMI(self,address):
        try:
            self._JMPFlag = self._ACC == self._memory[self._memory[address]]
        except:
                print("ERROR")
    
    def JPE(self,line):
        if self._JMPFlag:
            self._linePntr = line
        self._JMPFlag = None
    
    def JPN(self,line):
        if self._JMPFlag == False:
            self._linePntr = line
        self._JMPFlag = None

    def IN(self):
        self._ACC = ord(input())

    def OUT(self):
        print(ascii(self._ACC))
    
    def AND(self,operand):
        pass

    def END(self):
        sys.exit()

