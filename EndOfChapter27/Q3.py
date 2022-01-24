# python EndOfChapter27/Q3.py

#Part A
# QueueClass is a derived class of the abstract class NodeClass

#Part B
class NodeClass:
    def __init__(self):
        self.__data : str = ""
        self.__pointer : int = -1


    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data : str):
        self.__data = data
    

    @property
    def pointer(self) -> int:
        return self.__pointer

    @pointer.setter
    def pointer(self, pointer : int):
        self.__pointer = pointer
    


class QueueClass:
    def __init__(self):
        self.__queue = [NodeClass() for _ in range(50)]
        self.__head : int = 0
        self.__tail : int = 0

    def JoinQueue(self, data : str):
        self.__queue[self.__tail].data = data
        self.__queue[self.__tail].pointer = self.__tail + 1
        self.__tail += 1
    
    def LeaveQueue(self):
        data = self.__queue[self.__head].data
        self.__queue[self.__head].data = ""
        self.__head += 1
        return data
    
    def Print(self):
        pointer = self.__head
        while pointer <= self.__tail -1 :
            print("Data : {0} , Pointer : {1}".format(self.__queue[pointer].data, self.__queue[pointer].pointer) )
            pointer = self.__queue[pointer].pointer


queue = QueueClass()

for i in range(10):
    queue.JoinQueue(data = "hi {0}".format(i))

print(queue.LeaveQueue())
print(queue.LeaveQueue())
queue.Print()