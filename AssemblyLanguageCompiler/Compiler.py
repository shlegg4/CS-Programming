import pickle
import linecache
import sys

InstructionSet = {"LDD" : 1,"LDM" : 2,"LDI" : 3,"LDX" : 4,"LDR" : 5,"MOV" : 6,"STO" : 7,"STX" : 8,"STI" : 9, "ADD" : 10, "SUB" : 11,"INC" : 12,"DEC" : 13,"JMP" : 14,"CMP" : 15,"CMI" : 16,"JPE" : 17,"JPN" : 18,"IN" : 19,"OUT" : 20,"AND" : 21,"DEF" : 22,"END" : 100}
LookupTable = {}
    

class Source:
    def __init__(self,dir):
        self._dir = dir
        self._linePntr = 0
        self.maxLinePntr = 0
        self._ACCVal  = 0
        self._IX = 0
        self._CMPFlag = False

    def Read(self):
        EOF = False

        while EOF == False:
            line = "" 
            self._linePntr += 1
            line = linecache.getline(self._dir,self._linePntr)
            print(line)
            if line == "END":
                self.maxLinePntr = self._linePntr
                EOF = True

            #Syntax Analysis
            infixLine = []
            lexemes = line.split(" ")
            for lexeme in lexemes:
                try:
                    infixLine.append(InstructionSet[lexeme.replace("\n","")])
                except:
                    try:
                        LookupTable[lexeme.replace("\n","").replace("@","")]
                        infixLine.append(lexeme.replace("\n","").replace("@",""))
                    except:
                        if "#" in lexeme:
                            infixLine.append(lexeme.replace("\n",""))     #If value passed rather than address
                        elif "@" in lexeme:
                            infixLine.append(lexeme.replace("@","").replace("\n",""))
                        elif lexeme.replace("\n","") == "ACC" or lexeme.replace("\n","") == "IX":
                            infixLine.append(lexeme.replace("\n",""))
                        else:
                            print("Syntax Error encountered on line {0}.".format(self._linePntr))
                            sys.exit()
                      #return the address of the variable and append to infix line @ symbol used to represent address

                        

            #Execution
            if infixLine[0] == 1:   #LDD
                self._ACCVal = LookupTable[infixLine[1]]
            elif infixLine[0] == 2: #LDM
                infixLine[1] = infixLine[1].replace("#","")
                self._ACCVal = int(infixLine[1])
            elif infixLine[0] == 3: #LDI 
                address = str(LookupTable[infixLine[1]])
                self._ACCVal = LookupTable[address]
            elif infixLine[0] == 4: #LDX
                    self._ACCVal = int(LookupTable[str(int(infixLine[1]) + int(self._IX))])
            elif infixLine[0] == 5: #LDR
                self._IX = int(infixLine[1])
            elif infixLine[0] == 6: #MOV
                self._IX = self._ACCVal
                self._ACCVal = 0
            elif infixLine[0] == 7: #STO
                LookupTable[infixLine[1]] = self._ACCVal
            elif infixLine[0] == 8: #STX
                        LookupTable[str(int(infixLine[1]) + int(self._IX))] = self._ACCVal
            elif infixLine[0] == 9: #STI
                        address = str(LookupTable[infixLine[1]])
                        LookupTable[address] = self._ACCVal
            elif infixLine[0] == 10: #ADD
                    if '#' in infixLine [1]:
                        self._ACCVal += int(infixLine[1].strip('#'))
                    else:
                        self._ACCVal += LookupTable[infixLine[1]]
            elif infixLine[0] == 11: #SUB
                    if '#' in infixLine [1]:
                        self._ACCVal -= int(infixLine[1].strip('#'))
                    else:
                        self._ACCVal -= LookupTable[infixLine[1]]
            elif infixLine[0] == 12: #INC
                if infixLine[1] == "ACC":
                    self._ACCVal += 1
                elif infixLine[1] == "IX":
                    self._IX += 1
            elif infixLine[0] == 13: #DEC
                if infixLine[1] == "ACC":
                    self._ACCVal -= 1
                elif infixLine[1] == "IX":
                    self._IX -= 1
            elif infixLine[0] == 14: #JMP
                        self._linePntr = LookupTable[infixLine[1]] - 1
            elif infixLine[0] == 15: #CMP
                    if '#' in infixLine[1]:
                        if int(infixLine[1].strip('#')) == self._ACCVal:
                            self._CMPFlag = True
                    else:
                        value = LookupTable[infixLine[1]]
                        if value == self._ACCVal:
                            self._CMPFlag = True
                        else:
                            self._CMPFlag = False
            elif infixLine[0] == 16: #CMI
                        address = str(LookupTable[infixLine[1]])
                        value = LookupTable[address]
                        if value == self._ACCVal:
                            self._CMPFlag = True
                        else:
                            self._CMPFlag = False
            elif infixLine[0] == 17: #JPE
                if self._CMPFlag:
                    self._linePntr = LookupTable[infixLine[1]] -1
                    self._CMPFlag = False
            elif infixLine[0] == 18: #JPN
                if self._CMPFlag == False:
                    self._linePntr = LookupTable[infixLine[1]] - 1
                    self._CMPFlag  = False
            elif infixLine[0] == 19: #IN
                self._ACCVal = ord(input())
            elif infixLine[0] == 20: #OUT
                print(ascii(self._ACCVal))
            elif infixLine[0] == 21: #AND
                if '#' in infixLine[1]:
                    self._ACCVal = self._ACCVal & int(infixLine[1].strip('#'))
                else:
                        value = LookupTable[infixLine[1]]
                        self._ACCVal = self._ACCVal & value
            elif infixLine[0] == 22: #DEF
                LookupTable[infixLine[1]] = None
            
            elif infixLine[0] == 100: #END
                sys.exit()





                




                
                    


                


source = Source("AssemblyLanguageCompiler/SourceCode.txt")
source.Read()