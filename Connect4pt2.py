class DimensionError(Exception):
    pass


class Cell:
    def __init__(self, valueH = 1, valueV = 1, valueDL = 1, valueDR = 1, tag: int = 0):
        self._valueH = valueH
        self._valueV = valueV
        self._valueDL = valueDL
        self._valueDR = valueDR
        self._tag = tag
    def __eq__(self, other):
        return self._tag == other._tag
    
    def __iadd__(self, val: int):
        self._value += val
        return self
            
    def __str__(self):
        #return (f"ValueH = {self._valueH} ; ValueV = {self._valueV} ; valueDL = {self._valueDL} ; valueDR = {self._valueDR}; Tag = {self._tag} ")
        return f"Tag = {self._tag}"
        #return f"{self._valueH}"
    def __int__(self):
        return int(self._value)

class CellStack:
    def __init__(self, length):
        self._basePNTR = 0
        self._topPNTR = 0
        self._data = [Cell() for _ in range(length)]

    def Pop(self):
        self._data[self._topPNTR],res = None,self._data[self._topPNTR]
        self._topPNTR -= 1
        return res
    
    def Push(self, value):
        self._[self._topPNTR] = value
        self._topPNTR += 1

    def __getitem__(self, key):
        if isinstance(key, slice):
            slicer = key.indices(len(self._data))
            length = slicer[1] - slicer[0]
            stk = CellStack(length)
            stk._data = [self[i] for i in range(*slicer)]
            return stk
        else:
            return self._data[key]
    
    def __setitem__(self, key, value: Cell):
        self._data[key] = value
    
    def __str__(self):
        string = [f"{self._data[i]}" for i in range(len(self._data))]
        return "\n".join(string)
    
class Grid:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._data = [CellStack(self._rows) for _ in range(self._columns)]

    def add_item(self, tag, column):
        
        if column <= self._columns:

            self._data[column].Push(tag)
        else:
            raise DimensionError("Column %d is out of range" % column)
    

    def __getitem__(self,key):
        if isinstance(key[0], slice) and isinstance(key[1], slice):
            slicer1 = key[0].indices(len(self._data))
            slicer2 = key[1].indices(len(self._data))
            _rows = slicer1[1] - slicer1[0]
            _cols = slicer2[1] - slicer2[0]
            grid = Grid(_rows, _cols)
            grid._data = [self._data[i][slice(*slicer2)] for i in range(*slicer1)]
            return grid
        elif type(key[0]) == int and type(key[1]) == int:
            i, j = key
            return self._data[i][j]
        else:
            raise IndexError("Index was not provided correctly")
    
    def __setitem__(self, key, value: Cell):
        i, j = key
        self._data[i][j] = value

    def sum_surroundings(self, index):
        x, y = index
        neighbours = stk[max(x-1,0):min(x+2,stk._rows),max(0,y-1):min(stk._columns,y+2)]
        self[x,y]._valueH += neighbours[1,0]._valueH + neighbours[1,2]._valueH
        self[x,y]._valueV += neighbours[0,1]._valueV + neighbours[2,1]._valueV


    
    def __str__(self):
        string = ""
        for i in range(self._rows):
            string += "["
            for j in range(self._columns):
                string += f"{self[i,j]},"
            
            string = string[:-1]+"]\n"
        return string



stk = Grid(5,5)
stk[0,1] = Cell(tag = 2)
stk[2,1] = Cell(tag = 1)
newGrid = stk[:,1:4]
x,y = 2,1
stk.sum_surroundings((2,1))


print(stk)
print(newGrid)


                



    
        