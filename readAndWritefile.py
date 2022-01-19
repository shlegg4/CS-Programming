import pickle

class Car:
    def __init__(self,VehicleId:int,Registration ="",DateOfRegistration = None,EngineSize = 0,PurchasePrice = 0.00):
        self.VehicleId = VehicleId
        self.Registration = Registration
        self.DateOfRegistration = DateOfRegistration
        self.EngineSize = EngineSize
        self.PurchasePrice = PurchasePrice
    def __str__(self):
        return str(self.__dict__)

Cars = [Car(VehicleId=3,EngineSize=10,Registration="HW64 SAM") for i in range(10)]

def writeToBin(directory,list):
    with open(directory,"wb+")as File:
        for item in list:
            pickle.dump(item,File)

def readBin(directory):
    result = []
    with open(directory,"rb") as File:
        EOF = False
        while not EOF:
            try :
                result.append(pickle.load(File))
                EOF = True
            except:
                EOF = True
    return result

def randAccesswrite(directory,item:Car):
    with open(directory,"rb+") as file:
        address = hash(item.VehicleId)
        EOF = False
        i = address
        while EOF == False:
            try:
                file.seek(address*150)
                pickle.dump(item,file)
                EOF = True
            except:
                print('no room')
                EOF = True

def randAccessread(directory:str,ID:int):
    result:Car
    with open(directory,'rb') as file:
        exitLoop = False
        address = hash(ID)
        i = address
        while exitLoop == False:
            try:
                file.seek(i*150)
                result = pickle.load(file)
                i+=1
                exitLoop = True
            except:
                print("not found")
                exitLoop == True
    return result
def InsertData():
    if input("hello there would you like to give me some data?(Y/N)") == "Y":
        directory = input("please define directory for folder -->")
        VehicleId =  int(input("Please define the id of your car -->"))
        Registration = input("Please input your reg number -->")
        userCar = Car(VehicleId= VehicleId,Registration=Registration)
        randAccesswrite(directory,userCar)
        loop()
        return
    else:
        if input("Ok would you like me to show you some data?(Y/N)") == "Y":
            directory = input("Please input directory -->")
            VehicleId = int(input("Please input the id of the vehicle you are trying to find -->"))
            print(randAccessread(directory,VehicleId))
            loop()
            return
        else:
            return
def loop():
    if input("Would you like to go again?") == "Yes":
        InsertData()
    else:
        return

InsertData()