from numpy import sin, cos


class var:
    def __init__(self, value: float, derivative: float = 1):
        self.value = value
        self.derivative = derivative

    def __neg__(self):
        return var(-self.value, -self.derivative)

    def __add__(self, other):
        if isinstance(other, var):
            return var(self.value + other.value, self.derivative + other.derivative)
        else:
            return var(self.value + other, self.derivative)

    def __sub__(self, other):
        if isinstance(other, var):
            return var(self.value - other.value, self.derivative - other.derivative)
        else:
            return var(self.value - other, self.derivative)

    def __mul__(self, other):
        if isinstance(other, var):
            return var(self.value * other.value, self.derivative * other.value + self.value * other.derivative)
        else:
            obj = var(self.value * other, self.derivative * other)
            return obj

    def __truediv__(self, other):
        if isinstance(other, var):
            return var(self.value / other.value, (self.derivative * other.value - self.value * other.derivative)/(other.value**2))
        else:
            return var(self.value / other, self.derivative / other)

    def __pow__(self, other):
        return var(self.value ** other, self.derivative * other * self.value ** (other-1))

    @staticmethod
    def sin(x):
        if isinstance(x, var):
            return var(sin(x.value), x.derivative*cos(x.value))
        else:
            return var(sin(x), 0)

    @staticmethod
    def cos(x):
        if isinstance(x, var):
            return var(cos(x.value), x.derivative*-sin(x.value))
        else:
            return var(cos(x), 0)

    def __str__(self):
        return f"({self.value}, {self.derivative})"

    """Takes lambda function and returns function built for value. allows for recursive calls"""
    @staticmethod
    def function(eq):
        def modified(arg):
            x = arg if isinstance(arg, var) else var(arg)
            return eq(x)
        return modified


class Scanner:
    def __init__(self, list=[]):
        self._list = list

    def __add__(self, other):
        obj = Scanner(self._list[:])
        if isinstance(other, Scanner):
            obj._list.append((var.__add__, other._list))
        else:
            obj._list.append((var.__add__, other))
        return obj

    def __sub__(self, other):
        obj = Scanner(self._list[:])
        if isinstance(other, Scanner):
            obj._list.append((var.__sub__, other._list))
        else:
            obj._list.append((var.__sub__, other))
        return obj

    def __mul__(self, other):
        obj = Scanner(self._list[:])
        if isinstance(other, Scanner):
            obj._list.append((var.__mul__, other._list))
        else:
            obj._list.append((var.__mul__, other))
        return obj

    def __truediv__(self, other):
        obj = Scanner(self._list[:])
        if isinstance(other, Scanner):
            obj._list.append((var.__truediv__, other._list))
        else:
            obj._list.append((var.__truediv__, other))
        return obj

    def __pow__(self, other):
        obj = Scanner(self._list[:])
        obj._list.append((var.__pow__, other))
        return obj

    def __str__(self):
        output = ""
        for op in self._list:
            output += f"{op},"
        output = output[:-1]
        return output
    
    def __iter__(self):
        return self._list.__iter__()
    


class equation:
    def __init__(self, func):
        val = func(var(Scanner(["x"]), Scanner()))
        self._f = self._convert_To_Func(val.value)
        self._df = self._convert_To_Func(val.derivative)
        pass
    def evaluate(self,X):
        res = var(1,0)
        for op in self._f:
            if op == "x":
                operator, operand = (var.__mul__,var(X))
            else:
                operator = op[0]
                operand = op[1]
            res = operator(res,operand)
        return res

    def _convert_To_Func(operations):
        def f(x):
            res = var(1,0)
            for operation in operations:
                if operation == "x":
                    operator, operand = (var.__mul__,var(x))
                else:
                    operator, operand = operation
                res = operator(res,operand)
            return res
        return f

    def _simplify(operations):
        for i in range(0,len(operations)-1):
            pass
"""
Simplifying equations
If x*0 then remove from operation list
if x-x then remove from operation list
if x^0 if multiplying then remove if addition convert to 1
if log 1 then convert to 0 
"""


# eq = equation(lambda x: x*3*5 + 3*5)
# print(eq.evaluate(2))

f = var.function(lambda x: x ** 2 + x * 3 + 5)
print(f(4))
