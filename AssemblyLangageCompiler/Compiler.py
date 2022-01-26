import pickle
import linecache

InstructionSet = {"LDD" : 1,"q" : 2,"INC" : 3}
identifiers = {}
    

class Source:
    def __init__(self,dir):
        self._dir = dir
        self._linePntr = 0
        self.maxLinePntr = 0
        self._ACCVal  = 0
        self._IX = 0

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
                    infixLine.append(InstructionSet.get(lexeme))    #appends the instruction to infix line
                except:
                    try:
                        if "#" in lexeme:
                            infixLine.append(lexeme.strip("\n"))     #If value passed rather than address
                        elif "@" in lexeme:
                            infixLine.append(lexeme.strip('@'))
                        else:
                            infixLine.append(identifiers.get(lexeme.strip("\n")))   #return the address of the variable and append to infix line @ symbol used to represent address
                    except:
                        print("Syntax Error encountered on line {0}.".format(self._linePntr))

            #Execution
            if infixLine[0] == 1:   #LDD
                    with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        self._ACCVal = pickle.load(LookupTable)
            elif infixLine[0] == 2: #LDM
                self._ACCVal = infixLine[1].strip('#')
            elif infixLine[0] == 3: #LDI
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        address = pickle.load(LookupTable)
                        LookupTable.seek(address)
                        self._ACCVal = pickle.load(LookupTable)
            elif infixLine[0] == 4: #LDX
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1] + self._IX)
                        self._ACCVal = pickle.load(LookupTable)
            elif infixLine[0] == 5: #LDR
                self._IX = infixLine[1].strip('#')
            elif infixLine[0] == 6: #MOV
                self._IX = self._ACCVal
                self._ACCVal = 0
            elif infixLine[0] == 7: #STO
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        pickle.dump(self._ACCVal,LookupTable)
            elif infixLine[0] == 8: #STX
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1] + self._IX)
                        pickle.dump(self._ACCVal,LookupTable)
            elif infixLine[0] == 9: #STI
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        address = pickle.load(LookupTable)
                        LookupTable.seek(address)
                        pickle.dump(self._ACCVal,LookupTable)
            elif infixLine[0] == 10: #ADD
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                    if '#' in infixLine [1]:
                        self._ACCVal += infixLine[1].strip('#')
                    else:
                        LookupTable.seek(infixLine[1])
                        self._ACCVal += pickle.load(LookupTable)
            elif infixLine[0] == 11: #SUB
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                    if '#' in infixLine [1]:
                        self._ACCVal -= infixLine[1].strip('#')
                    else:
                        LookupTable.seek(infixLine[1])
                        self._ACCVal -= pickle.load(LookupTable)
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
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        self._linePntr = pickle.load(LookupTable) - 1
            elif infixLine[0] == 15: #CMP
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                    if '#' in infixLine[1]:
                        if int(infixLine[1].strip('#')) == self._ACCVal:
                            self._CMPFlag = True
                    else:
                        LookupTable.seek(infixLine[1])
                        value = pickle.load(LookupTable)
                        if value == self._ACCVal:
                            self._CMPFlag = True
                        else:
                            self._CMPFlag = False
            elif infixLine[0] == 16: #CMI
                with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        address = pickle.load(LookupTable)
                        LookupTable.seek(address)
                        value = int(pickle.load(LookupTable))
                        if value == self._ACCVal:
                            self._CMPFlag = True
                        else:
                            self._CMPFlag = False
            elif infixLine[0] == 17: #JPE
                if self._CMPFlag:
                    LookupTable.seek(infixLine[1])
                    self._linePntr = pickle.load(LookupTable) - 1
            elif infixLine[0] == 18: #JPN
                if self._CMPFlag == False:
                    LookupTable.seek(infixLine[1])
                    self._linePntr = pickle.load(LookupTable) - 1
            elif infixLine[0] == 19: #IN
                self._ACCVal = ord(input())
            elif infixLine[0] == 20: #OUT
                print(ascii(self._ACCVal))
            elif infixLine[0] == 21: #AND
                if '#' in infixLine[1]:
                    self._ACCVal = self._ACCVal & int(infixLine[1].strip('#'))
                else:
                    with open("AssemblyLanguageCompiler/Table.DAT","rb+") as LookupTable:
                        LookupTable.seek(infixLine[1])
                        value = pickle.load(LookupTable)
                        self._ACCVal = self._ACCVal & value
            elif infixLine[0] == 22: #DEF
                identifiers[infixLine[1]] = infixLine[3]
            




                




                
                    


                


source = Source("AssemblyLangageInterpreter/SourceCode.txt")
source.Read()