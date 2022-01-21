# python EndOfChapter27/Q3.py

#Part A
# QueueClass is a derived class of the abstract class NodeClass

#Part B
class NodeClass:
    def __init__(self):
        self.__data : str = ""
        self.__pointer : int = -1

    def SetData(self, data : str):
        self.__data = data
    
    def SetPointer(self, pointer : int):
        self.__pointer = pointer

    def GetData(self) -> str:
        return self.__data
    
    def GetPointer(self) -> int:
        return self.__pointer


class QueueClass:
    def __init__(self):
        self.__queue = [NodeClass for _ in range(50)]
        self.__head : int = -1
        self.__tail : int = -1

        