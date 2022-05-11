import datetime
import pickle





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

    @property
    def ItemsOnLoan(self):
        return(self.__itemsOnLoan)

    def UpdateItemsOnLoan(self, NumOfNewItemsOnLoan):
        self.__itemsOnLoan += NumOfNewItemsOnLoan
    
    @property
    def PrintDetails(self):
        print("{0}; {1}; {2}; {3}; ".format(self.__borrowerName,self.__borrowerID,self.__emailAddress,self.__itemsOnLoan))


class LibraryItem:

    def __init__(self, t, a ,i):
        self.__borrowerID = 0
        self.__title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__onLoan = False
        self.__dueDate = datetime.date.today()
    
    @property
    def Title(self):
        return(self.__title)
    
    @property
    def Creator(self):
        return(self.__Author__Artist)

    @property
    def ID(self):
        return(self.__ItemID)
    
    @property
    def OnLoan(self):
        return(self.__onLoan)

    @property
    def DueDate(self):
        return(self.__dueDate)



    def Borrowing(self,borrower : Borrower):
        if self.__onLoan == False:
            if borrower.ItemsOnLoan > 5:
                print("Too many books on loan return one to take one.")
            else:
                self.__borrowerID = borrower.ID
                borrower.UpdateItemsOnLoan(1)
                self.__onLoan = True
                self.__dueDate = self.__dueDate + datetime.timedelta(weeks= 3)
        else:
            print("Item is not in stock at current time")

    def Returning(self,borrower : Borrower):
        if borrower.ItemsOnLoan <= 0:
            print("No more books to return.")
            return
        else:
            borrower.UpdateItemsOnLoan(-1)
            self.__borrowerID = None
            self.__onLoan = False
    
    def PrintDetails(self):
        print("{0}; {1}; \n {2}; {3}; {4}".format(self.__title,self.__Author__Artist,self.__ItemID,self.__onLoan,self.__dueDate))

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self,t,a,i)
        self.__isRequested = False
        self.__isRequestedBy = 0 
    
    @property
    def IsRequested(self):
        return(self.__isRequested)
    
    
    def SetIsRequested(self,borrower : Borrower):
        self.__isRequestedBy = borrower.ID
        self.__isRequested = True

    def PrintDetails(self):
        LibraryItem.PrintDetails(self)
        print("Is requested : {0} ; Requested by : {1}".format(self.__isRequested,self.__isRequestedBy))


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self,t,a,i)
        self.__genre = ""

    @property
    def Genre(self):
        return(self.__genre)
    
    @Genre.setter
    def Genre(self,g):
        self.__genre = g

    def PrintDetails(self):
        super().PrintDetails()
        print(self.__genre)




class View:

    def __init__(self) -> None:
        print("1 - Add a new borrower")
        print("2 - Add a new book")
        print("3 - Add a new CD")
        print("4 - Borrow a book")
        print("5 - Return a book")
        print("6 - Borrow a CD")
        print("7 - Return a CD")
        print("8 - Request a Book")
        print("9 - Print all details")
        print("99 - Exit program")
        self.__choice = int(input("Please input your choice :"))

    @property
    def choice(self):
        return(self.__choice)


def Main():
    borrowers = [Borrower("","",0) for i in range(5)]
    books = [Book("","",0) for i in range(5)]
    cds = [CD ("","",0) for i in range(5)]


    while True:
        display = View()
        if display.choice == 1:
            """
            Create a new borrower object and append it to a database by using the borrowers id 
            """
            borrowerName = input("Please input borrower name : ")
            borrowerEmailAddress = input("Please input borrower email address : ")
            borrowerID = int(input("Please input borrower ID : "))
            borrower = Borrower(borrowerName=borrowerName,emailAddress = borrowerEmailAddress,borrowerID=borrowerID)
            borrowers[locate(borrower.ID,borrowers)] = borrower
        elif display.choice == 2:
            """
            Create a new book object and append it to a database by using the book id
            """
            title = input("Please input book title : ")
            author = input("Please input book author : ")
            bookID = int(input("Please input book ID : "))
            book = Book(title,author,bookID)
            books[locate(book.ID,books)] = book
        elif display.choice == 3:
            """
            Create a new CD and append it to a database by using cd id
            """
            title = input("Please input CD name : ")
            artist = input("Please input artists name : ")
            cdID = int(input("Please input cd ID : "))
            cd = CD(title,artist,cdID)
            cds[locate(cd.ID,cds)] = cd
        elif display.choice == 4:
            """
            Borrow a book by searching through database using locate function 
            """
            borrowerID = int(input("Please input borrower ID : "))
            indexborrower = locate(borrowerID,borrowers)
            bookID = int(input("Please input book id : "))
            indexbook = locate(bookID,books)
            books[indexbook].Borrowing(borrowers[indexborrower])
        elif display.choice == 5:
            """
            Return a book by searching database using locate function 
            """
            borrowerID = int(input("Please input borrower ID : "))
            indexborrower = locate(borrowerID,borrowers)
            bookID = int(input("Please input book id : "))
            indexbook = locate(bookID,books)
            books[indexbook].Returning(borrowers[indexborrower])
        elif display.choice == 6:
            """
            
            """
            borrowerID = int(input("Please input borrower ID : "))
            indexborrower = locate(borrowerID,borrowers)
            cdID = int(input("Please input cd id : "))
            indexcd = locate(cdID,cds)
            cds[indexcd].Borrowing(borrowers[indexborrower])
        elif display.choice == 7:
            borrowerID = int(input("Please input borrower ID : "))
            indexborrower = locate(borrowerID,borrowers)
            cdID = int(input("Please input cd id : "))
            indexcd = locate(cdID,cds)
            cds[indexcd].Returning(borrowers[indexborrower])
        elif display.choice == 8:
            borrowerID = int(input("Please input borrower ID : "))
            indexborrower = locate(borrowerID,borrowers)
            bookID = int(input("Please input book id : "))
            indexbook = locate(bookID,books)
            books[indexbook].SetIsRequested(borrowers[indexborrower])
        elif display.choice == 9:
            for borrower in borrowers:
                borrower.PrintDetails
            for cd in cds:
                cd.PrintDetails()
            for book in books:
                book.PrintDetails()
        elif display.choice == 99:
            break
        else:
            print("Not a valid input")
        

def locate(mode : bool,file : str):
    try:
        index = 0
        with open(file,"rb+") as file:
            try:
                file.seek(1)
                index = pickle.load(file)
            except:
                index = 0
                pickle.dump(index)
            while True:
                if mode:
                    file.seek(index)
                    try:
                        temp =pickle.load(file)
                        index += 1
                    except:
                        return index



    except:
        print("No file at location")
        return
        

Main()




"""
Main -> View -> View.choice returned -> Compare View.choice against defined values ->

If value chosen is add a borrower 
-> Borrower attributes inputted 
-> Borrower id  : Int , Borrowers : [Borrower] passed to locate function
-> Locate function checks if 












"""