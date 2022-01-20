
tickets = {"Breezer" : 4 , "Junior" : 0, "YoungAdult" : 2, "Adult" : 3}


class SeasonTicketHolder:
    def __init__(self,accountHolderName : str, accountHolderEmail : str):
        self.__accountHolderName = accountHolderName
        self.__accountHolderEmail = accountHolderEmail



class PayAsYouGoTicketHolder(SeasonTicketHolder):
    def __init__(self, accountHolderName: str, accountHolderEmail: str):
        super().__init__(accountHolderName, accountHolderEmail)
        self.__balance = 0 
    
    def PurchaseTicket(self,ticketType):
        try:
            price = tickets.get(ticketType)
        except:
            print("Not a valid ticket")
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
    
