import pickle
import datetime
import sys

curPointer : int = 0
ConstCellSize : int = 250
directory = "Database.DAT"
with open(directory,"rb+")as file:
    try:
        file.seek(0)
        curPointer = pickle.load(file)
        file.seek(5) 
        ConstCellSize = pickle.load(file)
    except:
        file.seek(0)
        pickle.dump(curPointer,file)
        file.seek(5) 
        pickle.dump(ConstCellSize,file)


class Borrower:
    
    def __init__(self,name,email) -> None:
        global curPointer
        global ConstCellSize
        self.__CellSize = ConstCellSize
        self.id = curPointer
        curPointer += 1
        self.name = name
        self.email = email
        self._itemsOnLoan = 0

    
    
    
    def updateItemsOnLoan(self,val):
        self._itemsOnLoan += val
        with open(directory,"rb+") as database:
            database.seek(self.id*self.__CellSize)
            pickle.dump(self,database)

    @property
    def CellSize(self):
        return self.__CellSize
    
    def __str__(self) -> str:
        return "id :{0}, name : {1}, email : {2}, itemsOnLoan : {3} ".format(self.id,self.name,self.email,self._itemsOnLoan)

class LibraryItem:
    __CellSize = ConstCellSize
    def __init__(self, title , AuthorArtist, onLoan) -> None:
        global curPointer
        
        self._title = title
        self._AuthorArtist = AuthorArtist
        self.id = curPointer 
        curPointer += 1
        self.onLoan = False
        self._dueDate = datetime.datetime.today()
        self._isRequested = False
        self._requesterID = -1
        self._borrowerID = -1

    def borrow(self,borrowerID):
        global directory
        if self.onLoan == False:
            self._borrowerID = borrowerID
            self.onLoan = True
            self._dueDate += datetime.timedelta(weeks=3)
            borrower = search(directory,self._borrowerID)
            borrower.updateItemsOnLoan(1)

            with open(directory,"rb+") as database:
                database.seek(self.id*self.__CellSize)
                pickle.dump(self,database)
        else:
            if input("Book is already on loan would you liked to request it (Y/N) : ") == "Y":
                self._isRequested = True
                self._requesterID = borrowerID
                with open(directory,"rb+") as database:
                    database.seek(self.id*self.__CellSize)
                    pickle.dump(self,database)

    def Return(self,borrowerID):
        global directory
        if self.onLoan == True:
            self._borrowerID = -1
            self.onLoan = False
            self._dueDate = datetime.datetime.today()

            borrower = search(directory,borrowerID)
            borrower.updateItemsOnLoan(-1)

            with open(directory,"rb+") as database:
                database.seek(self.id*self.__CellSize)
                pickle.dump(self,database)
        else:
            print("This book is not currently on loan")
            
    
    @property
    def CellSize(self):
        return self.__CellSize

    def __str__(self) -> str:
        return "id :{0}, title : {1}, AuthorArtist : {2}, onLoan : {3}, DueDate : {4} ".format(self.id,self._title,self._AuthorArtist,self.onLoan,self._dueDate)

class Book(LibraryItem):
    def __init__(self, title, AuthorArtist, onLoan) -> None:
        super().__init__(title, AuthorArtist, onLoan)
        

class CD(LibraryItem):
    def __init__(self, title, AuthorArtist, onLoan,genre) -> None:
        super().__init__( title, AuthorArtist, onLoan)
        self._genre = genre


def addBorrower(directory,borrower : Borrower):
    with open(directory,"rb+") as database:
        try:
            database.seek(borrower.id*borrower.CellSize+11)
            pickle.dump(borrower,database)
        except:
            print("No file at directory")

def addBook(directory,book : Book):
    with open(directory,"rb+") as database:
        try:
            database.seek(book.id*book.CellSize+11)
            pickle.dump(book,database)
        except:
            print("No file at directory")

def addCD(directory,CD : CD):
    with open(directory,"rb+") as database:
        try:
            database.seek(CD.id*CD.CellSize+11)
            pickle.dump(CD,database)
        except:
            print("No file at directory")

def search(directory,id):
    with open(directory,"rb+") as database:
        try:
            database.seek(id*ConstCellSize+11)
            item = pickle.load(database)
            return item
        except:
            print("File not found ")


class leafNode:
    def __init__(self,leafID,rightPNTR,leftPNTR,refPNTR) -> None:
        self.leafID : int= leafID
        self.rightPNTR : int = rightPNTR
        self.leftPNTR : int = leftPNTR
        self.refPNTR : int = refPNTR
    
    def traverse(self, inputID : int):
        if self.leafID >= inputID :
            return self.leftPNTR
        else:
            return self.rightPNTR

class BinaryTree:
    def __init__(self,directory) -> None:
        self._dataBaseDir = directory
        self._startPNTR = curPointer
        pass
        

    def InsertNode(self,inputID):
        global curPointer
        #try:
        with open(self._dataBaseDir,"rb+") as database:
            curPNTR = self._startPNTR
            while curPNTR != -1:
                database.seek(curPNTR)
                try:
                    leaf = pickle.load(database)
                    previousPNTR = curPNTR
                    curPNTR = leaf.traverse(inputID)       
                except:
                    pickle.dump(leafNode(inputID,-1,-1,-1),database)
                    curPNTR = -1
            try:
                if leaf.leafID >= inputID:
                    leaf.leftPNTR = curPointer
                else:
                    leaf.rightPNTR = curPointer
                pickle.dump(leaf,database)
                database.seek(curPointer)
                pickle.dump(leafNode(inputID,-1,-1,-1),database)
            except:
                print('First Entry') 

            
            curPointer += sys.getsizeof(leafNode) + 5
        #except:
            #print("No file at directory")
        
    def PrintTree(self):
        curPNTR = self._startPNTR
        

class View:

    def __init__(self) -> None:
        print("1 - Add a new borrower")
        print("2 - Add a new book")
        print("3 - Add a new CD")
        print("4 - Borrow a book")
        print("5 - Return a book")
        print("6 - Borrow a CD")
        print("7 - Return a CD")
        
        print("9 - Print all details")
        print("99 - Exit program")
        self.__choice = int(input("Please input your choice : "))

    @property
    def choice(self):
        return(self.__choice)


def Main():
    
    directory = "File.DAT"
    while True:
        display = View()
        if display.choice == 1:
            """
            Create a new borrower object and append it to a database by using the borrowers id 
            """
            borrowerName = input("Please input borrower name : ")
            borrowerEmailAddress = input("Please input borrower email address : ")
            borrower = Borrower(name=borrowerName,email=borrowerEmailAddress)
            addBorrower(directory,borrower)

        elif display.choice == 2:
            """
            Create a new book object and append it to a database by using the book id
            """
            title = input("Please input book title : ")
            author = input("Please input book author : ")
            book = Book(title,author,False)
            addBook(directory,book)
        elif display.choice == 3:
            """
            Create a new CD and append it to a database by using cd id
            """
            title = input("Please input CD name : ")
            artist = input("Please input artists name : ")
            genre = input("Please input music genre : ")
            cd = CD(title,artist,False,genre)
            addCD(directory,cd)
        elif display.choice == 4:
            """
            Borrow a book by using borrow function in library item
            """
            borrowerID = int(input("Please input borrower ID : "))
            bookID = int(input("Please input book id : "))
            book = search(directory,bookID)
            book.borrow(borrowerID)

        elif display.choice == 5:
            """
            Return a book by searching database using locate function 
            """
            borrowerID = int(input("Please input borrower ID : "))
            bookID = int(input("Please input book id : "))
            book = search(directory,bookID)
            book.Return(borrowerID)

        elif display.choice == 6:
            """
            Borrow a CD
            """
            borrowerID = int(input("Please input borrower ID : "))
            cdID = int(input("Please input cd id : "))
            cd = search(directory,cdID)
            cd.borrow(borrowerID)

        elif display.choice == 7:
            """
            Return a cd
            """
            borrowerID = int(input("Please input borrower ID : "))
            cdID = int(input("Please input cd id : "))
            cd = search(directory,cdID)
            cd.Return(borrowerID)

        elif display.choice == 9:
            print("library details: ")
            for i in range(curPointer):
                print(search(directory,i))


        elif display.choice == 99:
            with open(directory,"rb+")as file:
                file.seek(0)
                pickle.dump(curPointer,file)
                file.seek(5) 
                pickle.dump(ConstCellSize,file)
            break
        else:
            print("Not a valid input")
        



Main()