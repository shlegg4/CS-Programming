"""
1. Partial differentiation
2. Cross Product
3. Unit Vector
4. Rendering


1.
    Group values in tuple (value,derivative)
    Chaining expression allows to simoultaneously calculate values and derivative
"""

#Differentiation Module

""" 
A contains value and derivative
dito B
result is A+B , derivative of A + derivative of B

"""
import numpy as np
import time
import math
import os

class val: 
    def __init__(self,value : float,derivative : float = 1): 
        self.value = value
        self.derivative = derivative

    def __neg__(self):
        return val(-self.value,-self.derivative)

    def __add__(self,other):
        if isinstance(other,val):
            return val(self.value + other.value, self.derivative + other.derivative)
        else:
            return val(self.value + other, self.derivative)
    
    def __sub__(self,other):
        if isinstance(other,val):
            return val(self.value - other.value, self.derivative - other.derivative)
        else:
            return val(self.value - other, self.derivative)
    
    def __mul__(self,other):
        if isinstance(other,val):
            return val(self.value * other.value, self.derivative * other.value + self.value * other.derivative)
        else:
            return val(self.value * other, self.derivative * other)
    
    def __truediv__(self,other):
        if isinstance(other,val):
            return val(self.value / other.value, (self.derivative * other.value - self.value * other.derivative)/(other.value**2))
        else:
            return val(self.value / other, self.derivative / other)
    
    def __pow__(self, other):
            return val(self.value ** other, self.derivative * other * self.value ** (other-1))
    
    @staticmethod
    def sin(x):
        if isinstance(x,val):
            return val(np.sin(x.value),x.derivative*np.cos(x.value))
        else:
            return val(np.sin(x),0)
    
    @staticmethod
    def cos(x):
        if isinstance(x,val):
            return val(np.cos(x.value),x.derivative*-np.sin(x.value))
        else:
            return val(np.cos(x),0)
    
    def __str__(self):
        return f"({self.value},{self.derivative})"

def param(t,s):
    x = (val.cos(t) + 2)*val.cos(s)
    y = (val.cos(t) + 2)*val.sin(s)
    z = val.sin(t)
    return((x.value,y.value,z.value),(x.derivative,y.derivative,z.derivative))

def norm(tVal, sVal):
    start = time.perf_counter()
    t = val(tVal, 1)
    s = val(sVal, 0)
    dt = param(t, s)[1]
    t = val(tVal, 0)
    s = val(sVal, 1)
    point ,ds = param(t, s)
    norm = np.cross(np.array(dt),np.array(ds))
    elapsed = time.perf_counter() - start
    #print(f"{elapsed = } seconds")
    return norm,point

def render(xAngle = 0,zAngle = 0):
    output = [[" " for _ in range(50)] for _ in range(50)]
    Min = -10
    Max = 10
    for t in np.linspace(0,2*math.pi,60):
        for s in np.linspace(0,2*math.pi,60):
            normal, point = norm(t,s)
            #try:
            light = np.array((-1,-1,-1))
            Luminance = round((np.dot(normal,light)/(np.sqrt(np.dot(normal,normal))*np.sqrt(np.dot(light,light)))*11))
            Luminance = max(Luminance,0)
            point = np.array([[1,0,0],[0,1,1]])@np.array([[np.cos(xAngle),-np.sin(xAngle),0],[np.sin(xAngle),np.cos(xAngle),0],[0,0,1]])@np.array([[1,0,0],[0,np.cos(zAngle),-np.sin(zAngle)],[0,np.sin(zAngle),np.cos(zAngle)]]) @ point
            x , y = round((point[0]-Min)/(Max-Min)*49) , round((point[1]-Min)/(Max-Min)*49)
            output[x][y] = "`.,-~:;=!*#$@"[Luminance] if output[x][y] == " " else output[x][y]
            #except:
             #   pass
    #os.system("clear")
    for x in output:
        for i,y in enumerate(x):
            print(f"{y}",end="")
        print("")


for i in range(50):
    render(0,i*0.1)
    time.sleep(0.5)
    
    
