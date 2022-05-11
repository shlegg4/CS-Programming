instructions = {}
Include = lambda x : instructions.setdefault(x.__name__,x)


@Include
def hello():
    print("Hello!")






"""
RPN (reverse polish notation)

Radix line, Infix Line, something else

"""


