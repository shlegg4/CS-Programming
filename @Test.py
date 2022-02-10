
data = {}

Task = lambda x : data.setdefault(x.__name__,x)

@Task
def F1(x,y):
    return x+y


print(data["F1"](2,3))