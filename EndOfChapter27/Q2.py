import datetime



tickets = {"Breezer" : 4 , "Junior" : 0, "YoungAdult" : 2, "Adult" : 3}
# dictionary to supply all possible ticket types and there corresponding values

class SeasonTicketHolder:
    def __init__(self,accountHolderName : str, accountHolderEmail : str):
        self.__accountHolderName = accountHolderName
        self.__accountHolderEmail = accountHolderEmail



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
            depositAmount = input("Account overdrawn on purchase. Deposit required")
            self.Deposit(depositAmount)

    def Deposit(self,amount):
        self.__balance += amount

class ContractTicketHolder(SeasonTicketHolder):
    def __init__(self, accountHolderName: str, accountHolderEmail: str, fixedFee : int = 20):
        super().__init__(accountHolderName, accountHolderEmail)
        self.__fixedFee = fixedFee
        self.__monthOfLastPayment = datetime.date.today().month
    
    def PayContract(self):
        curMonth = datetime.date.today().month
        owed = (curMonth - self.__monthOfLastPayment)*self.__fixedFee
        print("Owed : {0}".format(owed))


newCustomer = ContractTicketHolder("A.Smith","xyz@abc.xx",10)
    
