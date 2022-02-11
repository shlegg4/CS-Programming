cars = ["Aston Martin","BMW","VW"]
for i,val in enumerate(cars):
    print(f"Index Position : {i} , Value : {val}")

carList = list(enumerate(cars))
print(carList)

Car1 , Car2 , Car3 = *cars

