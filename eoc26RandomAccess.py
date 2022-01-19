import pickle


class CustomerRecord():
    def __init__(self, telephoneNo: str, name: str, orderValue: float,
                 customerId: int):
        if len(telephoneNo) != 14 or len(
                name) > 30 or 100001 > customerId or customerId > 999999:
            print(
                "Type Error encountered  length of phone number {0} != 14  , name  {1} needs to be < 30"
                .format(len(telephoneNo), len(name)))
        else:
            self.customerId = customerId
            self.telephoneNo = telephoneNo
            self.name = name
            self.orderValue = orderValue

    def __str__(self):
        return str(self.__dict__)


class Database():
    def __init__(self, directory: str):  #initialise database
        self.directory = directory

    def storeData(self, address: int, customer: CustomerRecord):
        with open(self.directory, "rb+") as file:
            file.seek(address * 70 + 1)
            pickle.dump(customer, file)

    def addRecord(self, customer: CustomerRecord):  #Add record to database
        id = customer.customerId
        address = Hash(id)
        addressFound = False
        i = address
        while addressFound == False:  # avoiding collisions
            with open(self.directory , "rb+") as file:
                
                file.seek(70*i+1)
              
                """ try: """
                record = pickle.load(file)
                if type(record) != CustomerRecord:
                    pickle.dump(customer,file)
                else:
                        i+=1
            """ except EOFError: """
            addressFound = True


    def findRecord(self, customerId):
        address = Hash(customerId)
        exitLoop = False
        i = address
        with open(self.directory,"rb") as file:
            while exitLoop == False:
                file.seek(70*(i)+1)
                #try:
                record = pickle.load(file)
                print("get duped")
                if record.customerId == customerId:
                    return pickle.load(file)
                else:
                    i+=1
                #except:
                exitLoop = True
                
            
        print("record not in database")


def Hash(customerID: int):
    Address = customerID % 1000
    return Address


CustomerData = Database("Directory.DAT")

customer = CustomerRecord("12345678912345", "TJ", 100.50, 100005)

CustomerData.addRecord(customer)
print(CustomerData.findRecord(100005))
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
