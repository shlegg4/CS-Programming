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

    
