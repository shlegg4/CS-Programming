

def divisor(divisor,dividend):
    try:
        return dividend/divisor
    except:
        print("divisor cant equal 0")
printString(0,6)


""" 


def Factorial(x):
    global CallNumber
    CallNumber+=1
    print(CallNumber,x)
    if x == 0:
        result = 1
    else:
        result = x*Factorial(x-1)
    print(result)
    return result

 CallNumber =0 
answer = Factorial(3)

print(answer) 

def exponent(base,exp):
    Result = 1
    for i in range(exp):
        print(i)
        Result = Result * base
    return Result

print(exponent(2,3))

def Fibbonacci(n):
    if n ==0 or n==1:
        result = 1
    else:
        result = Fibbonacci(n-1) + Fibbonacci(n-2)
    return result

for i in range(5):
  print(Fibbonacci(i))

 def CountDown(n):
    if n == 0:
        print(n)
    else:
        print(n)
        CountDown(n-1)
def CountUp(n):
    if n == 0:
        print(n)
    else:
        CountUp(n-1)
        print(n)
        
def X(n):
    if n==0 or n==1:
        print (n)
    else: 
        X(n//2)
        print( n%2)


X(19)

def GCD(a,b):
    if a>b:
        quotient = a//b
        remainder = a%b
        if remainder == 0:
            return b
        else:
            GCD(b,remainder)


 """ 