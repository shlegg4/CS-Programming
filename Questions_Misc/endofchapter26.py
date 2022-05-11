import pickle


class CustomerRecord():
    def __init__(self,telephoneNo : str, name : str, orderValue : float,customerId : int):
        if len(telephoneNo) != 14 or len(name) > 30 or 100001 > customerId or customerId > 999999:
           print("Type Error encountered  length of phone number {0} != 14  , name  {1} needs to be < 30".format(len(telephoneNo),len(name)))
        else:
            self.customerId = customerId
            self.telephoneNo = telephoneNo
            self.name = name
            self.orderValue = orderValue
    def __str__(self):
        return str(self.__dict__)

    

class Database():
    def __init__(self,directory:str):       #initialise database
        self.dataBase = [0 for i in range(999)]
        self.directory = directory


    def __storeData(self,dataItem,address):
        with open(self.directory,"wb+") as file:
            file.seek(address)
            pickle.dump(dataItem,self.directory)


    def addRecord(self,customer : CustomerRecord):      #Add record to database
        id = customer.customerId
        address = Hash(id)
        adressFound = False
        
        while adressFound == False:     # avoiding collisions
            if type(self.dataBase[address]) == CustomerRecord:
                address += 1
            else:
                self.dataBase[address] = customer
                adressFound = True
        self.__storeData(customer,address)
    
    def findRecord(self,customerId):
        address = Hash(customerId)
        if type(self.dataBase[address]) == CustomerRecord:
            return self.dataBase[address]
        else:
            print("No record at location")


def Hash(customerID : int):
    Address = customerID % 1000
    return Address



CustomerData = Database("CustomerData.DAT")

customer = CustomerRecord("12345678912345","TJ",100.50,100005)

CustomerData.addRecord(customer)
print(CustomerData.findRecord(5))



"""

d)
In order for the company to implement a random-access file system to store customer records they would have to 
open a file to be used for random access writing and reading they would then have to save a record to the file.
The company would also have to define the save of each record in memory otherwise python will overwrite portions 
of other records when it tries to save a new one. By defining the size of a record python can increment the address' of
where its saving records properly so that.
"""

def accessFile():
    directory = input("Which file do you want to use? ")
    try:
        with open(directory, "rb") as file:
            print("Opened")
    except:
        print("No file at location")
        
