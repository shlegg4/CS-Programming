#python EndOfChapter27/Q2.py


"""
B)
i) The season ticket holder attributes are declared private so that they can only be accessed using their getter and setter methods this makes the class more robust as attribute like ticketholdername cant be modified when the class is instantiated
i) The methods are declared as public so that they can be accessed for manipulating attriutes without the attributes ever being directly manipulated


"""


import datetime



tickets = {"Breezer" : 4 , "Junior" : 0, "YoungAdult" : 2, "Adult" : 3}
# dictionary to supply all possible ticket types and there corresponding values

class SeasonTicketHolder:
    def __init__(self,accountHolderName : str, accountHolderEmail : str):
        self.__accountHolderName = accountHolderName
        self.__accountHolderEmail = accountHolderEmail

    def __str__(self) -> str:
        return "Account Holder Name : {0} , Account Holder Email : {1} ,".format(self.__accountHolderName ,self.__accountHolderEmail)

    def Print(self):
        print(self)

class PayAsYouGoTicketHolder(SeasonTicketHolder):
    def __init__(self, accountHolderName: str, accountHolderEmail: str):
        super().__init__(accountHolderName, accountHolderEmail)
        self.__balance = 0 
    
    # Purchasing a ticket requires supplying a valid ticket from the global dictionary supplied at top of file 
    
    def PurchaseTicket(self,ticketType):
        try:
            price = tickets.get(ticketType) # Inside try except block in order to detect whether or not a valid ticket is supplied
        except:
            print("Not a valid ticket")
            return
        if(self.__balance - price > 0):
            self.__balance -= price
        else:
            depositAmount = input("Account overdrawn on purchase. Deposit required : ")
            self.Deposit(depositAmount)

    def Deposit(self,amount):
        self.__balance += int(amount)

    def __str__(self) -> str:
        return super().__str__() + " Balance : £{0}".format(self.__balance)

class ContractTicketHolder(SeasonTicketHolder):
    def __init__(self, accountHolderName: str, accountHolderEmail: str, fixedFee : int = 20):
        super().__init__(accountHolderName, accountHolderEmail)
        self.__fixedFee = fixedFee
        self.__monthOfLastPayment = datetime.date.today().month
    
    def PayContract(self):
        curMonth = datetime.date.today().month
        owed = (curMonth - self.__monthOfLastPayment)*self.__fixedFee
        print("Owed : {0}".format(owed))

    def __str__(self) -> str:
        return super().__str__() + " Fixed Fee : £{0} , Month OF Last Payment : {1}".format(self.__fixedFee,self.__monthOfLastPayment)
    
    



FirstCustomer = PayAsYouGoTicketHolder("Sam", "Sam@ryde")
FirstCustomer.Deposit(5)
FirstCustomer.PurchaseTicket("Breezer")
FirstCustomer.PurchaseTicket("Breezer")
FirstCustomer.Print()
SecondCustomer = ContractTicketHolder("TJ","TJ@ryde",10)
SecondCustomer.Print()

