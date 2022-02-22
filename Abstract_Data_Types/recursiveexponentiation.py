def power(x,n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return power(x,n-1) * x

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return factorial(x-1) * x 








