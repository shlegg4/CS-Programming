total = 5050    #The sum from 0 to 100

array = [i for i in range(101)]
array.remove(96)
count = 0
for i in range(50):
    count += array[i] + array[99-i]

missingElement = total - count
print(missingElement)

def reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse(string[:-1])
    
a = "hello world"
print(reverse(a))
