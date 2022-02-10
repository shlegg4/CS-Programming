import datetime


class HiddenBox:
    # __BoxName : string
    # __Creator : string
    # __DateHidden : string
    # __GameLocation : string
    # __LastFinds : [[string]]
    # __Active : boolean

    def __init__(self,boxName,creator,dateHidden,gameLocation): 
        self.__BoxName = boxName
        self.__Creator = creator
        self.__DateHidden = dateHidden
        self.__GameLocation = gameLocation
        self.__Active = False
        self.__LastFinds = []

    def GetBoxName(self):
        return self.__BoxName
    
    def GetGameLocation(self):
        return self.__GameLocation

class PuzzleBox(HiddenBox):
    def __init__(self,puzzleText,solution,boxName,creator,dateHidden,gameLocation):
        super().__init__(boxName,creator,dateHidden,gameLocation)
        self.__PuzzleText = puzzleText
        self.__Solution = solution


def NewBox(numBoxes):
    global TheBoxes
    boxName = input("Please enter a box name : ")
    creator = input("Please enter a creator : ")
    dateHidden = input("Please enter a date hidden : ")
    gameName = input("Please enter a game location : ")
    TheBoxes[numBoxes] = HiddenBox(boxName, creator, dateHidden, gameName)
    numBoxes += 1
    return numBoxes

TheBoxes = [HiddenBox("","","","") for _ in range(10000)]
numBoxes = 0
numBoxes = NewBox(numBoxes)



