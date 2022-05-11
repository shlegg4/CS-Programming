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
    def BorrowerID(self):
        return(self.__borrowerID)

    @property
    def ItemsOnLoan(self):
        return(self.__itemsOnLoan)

    def UpdateItemsOnLoan(self, NumOfNewItemsOnLoan):
        self.__itemsOnLoan += NumOfNewItemsOnLoan
    
    @property
    def PrintDetails(self):
        print("{0}; {1}; {2}; {3}; ".format(self.__borrowerName,self.__borrowerID,self.__emailAddress,self.__itemsOnLoan))


borrower = Borrower("Sam","15slegg@rydeschool.net","4")

print(borrower.BorrowerName)
borrower.UpdateItemsOnLoan(3)
borrower.PrintDetails