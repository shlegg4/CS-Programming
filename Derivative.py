from numpy import sin , cos
class var: 
    def __init__(self,value : float,derivative : float = 1): 
        self.value = value
        self.derivative = derivative

    def __neg__(self):
        return var(-self.value,-self.derivative)

    def __add__(self,other):
        if isinstance(other,var):
            return var(self.value + other.value, self.derivative + other.derivative)
        else:
            return var(self.value + other, self.derivative)
    
    def __sub__(self,other):
        if isinstance(other,var):
            return var(self.value - other.value, self.derivative - other.derivative)
        else:
            return var(self.value - other, self.derivative)
    
    def __mul__(self,other):
        if isinstance(other,var):
            return var(self.value * other.value, self.derivative * other.value + self.value * other.derivative)
        else:
            return var(self.value * other, self.derivative * other)
    
    def __truediv__(self,other):
        if isinstance(other,var):
            return var(self.value / other.value, (self.derivative * other.value - self.value * other.derivative)/(other.value**2))
        else:
            return var(self.value / other, self.derivative / other)
    
    def __pow__(self, other):
            return var(self.value ** other, self.derivative * other * self.value ** (other-1))
    
    @staticmethod
    def sin(x):
        if isinstance(x,var):
            return var(sin(x.value),x.derivative*cos(x.value))
        else:
            return var(sin(x),0)
    
    @staticmethod
    def cos(x):
        if isinstance(x,var):
            return var(cos(x.value),x.derivative*-sin(x.value))
        else:
            return var(cos(x),0)
    
    def __str__(self):
        return f"({self.value},{self.derivative})"

    """Takes lambda function and returns function built for value. allows for recursive calls"""
    @staticmethod
    def equation(eq):
        def modified(arg):
            x = arg if isinstance(arg,var) else var(arg)
            return eq(x)
        return modified


eq = var.equation(lambda x : x * 2 + 3)
j = eq(4)
f = var.equation(lambda x: eq(x) + x*3)
print(f(3))
