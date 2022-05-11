import pickle
import sys
from typing import Any
class Borrower:

    def __init__(self,borrowerName,emailAddress,borrowerID):
        self.__borrowerName = borrowerName
        self.__emailAddress = emailAddress
        self.__borrowerID = borrowerID
        self.__itemsOnLoan = 0

    @property
    def BorrowerName(self):
        return(self.__borrowerName)
    
    @property
    def ID(self):
        return(self.__borrowerID)
    
    def _GetID(self,value):
        self.__borrowerID = value

    @property
    def ItemsOnLoan(self):
        return(self.__itemsOnLoan)

    def UpdateItemsOnLoan(self, NumOfNewItemsOnLoan):
        self.__itemsOnLoan += NumOfNewItemsOnLoan
    
    @property
    def PrintDetails(self):
        print("{0}; {1}; {2}; {3}; ".format(self.__borrowerName,self.__borrowerID,self.__emailAddress,self.__itemsOnLoan))


def updateLibFile(dir : str,obj : Any):
    try:
        with open(dir,"rb+") as file:
            
            obj._GetID(int.from_bytes(bytes=file.read(4),byteorder="big",signed=False)) # convert header to int to use for id of object
            if obj.ID == 0:
                obj._GetID(5)
                file.write(obj.ID.to_bytes(4,byteorder="big",signed=False))
           
            file.seek(obj.ID) # seek to next available address
            pickle.dump(obj,file)

            nextAddress = obj.ID + sys.getsizeof(obj) + 2# classSize is equal to the number of bytes assigned to that object
            file.seek(0)
            file.write(nextAddress.to_bytes(4,byteorder="big",signed=False)) # update the next available address in the header of the file

    except:
        print("Fatal error occured!!!!!")    
        


    


borrower = Borrower("Sam","@Sam",0)
updateLibFile("CS-Programming/File.DAT",borrower)
with open("CS-Programming/File.DAT","rb") as file:
    file.seek(5)
    obj = pickle.load(file)
    print("hello")