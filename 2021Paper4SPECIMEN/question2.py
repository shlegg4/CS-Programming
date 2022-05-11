import re


class HiddenBox:
    """
    Declare _BoxName : STRING
    Declare _Creator : STRING
    Declare _DateHidden : STRING
    Declare _GameLocation : STRING
    Declare _LastFinds : [[STRING]]
    Declare _Active : BOOL
    """

    def __init__(self, BoxName = None, Creator = None, DateHidden = None, GameLocation = None): 
        self._Active = False
        self._BoxName = BoxName
        self._Creator = Creator
        self._DateHidden = DateHidden
        self._GameLocation = GameLocation
        self._LastFinds = ["" for _ in range(10)]


    def GetBoxName(self):
        return self._BoxName

    def GetGameLocation(self):
        return self._GameLocation



FreePNTR = 0
TheBoxes = [HiddenBox() for _ in range(10000)]

def NewBox(self, Name, Creator, DateHidden, GameLocation):
    TheBoxes[FreePNTR] = HiddenBox(Name, Creator, DateHidden, GameLocation)
    FreePNTR += 1

NewBox("","","","")

class puzzlebox(HiddenBox):
    """
    DECLARE PuzzleText : STRING
    DECLARE Solution : STRING
    """
    def __init__(self, PuzzleText, Solution, BoxName, Creator, DateHidden, GameLocation):
        self._PuzzleText = PuzzleText
        self._Solution = Solution
        self._Active = False
        self._BoxName = BoxName
        self._Creator = Creator
        self._DateHidden = DateHidden
        self._GameLocation = GameLocation
        self._LastFinds = ["" for _ in range(10)]
