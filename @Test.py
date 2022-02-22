import os
data = {}

Task = lambda x : data.setdefault(x.__name__,x)

@Task
def F1(x,y):
    return x+y


print(data["F1"](2,3))

data = [[0 for _ in range(5)] for _ in range(4)]
data.append([1,2,3])

print("hi")
os.system('cls' if os.name == 'nt' else 'clear')
