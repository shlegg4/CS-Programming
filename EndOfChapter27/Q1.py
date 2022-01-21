import datetime

class BankAccount:
    def __init__(self,accountHolderName : str , IBAN : int):
        self.__accountHolderName = accountHolderName
        self.__IBAN = IBAN

    @property
    def AccountHolderName(self):
        return self.__accountHolderName

    @AccountHolderName.setter
    def AccountHolderName(self,accountHolderName):
        self.__accountHolderName = accountHolderName

    @property
    def IBAN(self):
        return self.__IBAN
    
    @IBAN.setter
    def IBAN(self):
        return self.__IBAN
    
class SavingsAccount(BankAccount):
    def __init__(self, accountHolderName: str, IBAN: int, overDraftLimit : int, monthlyFee : int):
        super().__init__(accountHolderName, IBAN)
        self.__balance = 0
        self.__overDraftLimit = overDraftLimit
        self.__monthlyFee = monthlyFee
    
    @property
    def Balance(self):
        return self.__balance

    def Withdraw(self,amount : int):
        if(self.__overDraftLimit < self.__balance - amount):
            self.__balance -= abs(amount)   #Absolute value so that amount is only positive
        else:
            print("Account holder is beyond their allowable over draft. Please pay fine of £100")
            self.__balance -= 100

    def Deposit(self,amount : int):
        self.__balance += abs(amount)

    def PayMonthlyFee(self):
        self.__balance -= self.__monthlyFee

    
class PersonalAccount(BankAccount):
    def __init__(self, accountHolderName: str, IBAN: int, interestRate : float):
        super().__init__(accountHolderName, IBAN)
        self.__balance = 0 
        self.__interestRate = interestRate
        self.__curMonth = datetime.date.today().month

    def Deposit(self,amount):
        
        self.__curMonth = datetime.date.today().month
        self.__balance += self.__Interest() + amount
        
    
    def Withdraw(self,amount):
        if(self.__balance - amount > 0):
            self.__balance -= amount
            self.__balance += self.__Interest()
            self.__curMonth = datetime.date.today().month
        else:
            print("Unable to withdraw that amount of money as that would make account over drawn")

    def __Interest(self):
         # Calculate the number of months since last access of account and using this number calculate the amount of interest gained since last deposit
        interest = self.__balance*self.__interestRate**(datetime.date.today().month - self.__curMonth)
        return interest
    
            
        


myAccount = PersonalAccount("Samuel Legg","1234",1.01)
myAccount.Deposit(10)

