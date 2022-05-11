class Mat:
    __slots__ = ("_rows","_columns","_data")

    def __init__(self,data = None):
            if not(all(len(row) == len(data[0]) for row in data)):
                raise ValueError("Rows aren't all same length.")
            self._data = data
            self._rows = len(data)
            self._columns = len(data[0])
    
    def __add__(self,other):
        if (self._rows == other._rows and self._columns == other._columns):
            temp = Mat([[0 for i in range(self._columns)] for _ in range(self._rows)])
            for i in range(self._rows):
                for j in range(self._columns):
                    temp[i,j] = self[i,j] + other[i,j]
            return temp
        else:
            raise ValueError("Matrices must be of the same dimensions")
    
    def __sub__(self, other):
        if (self._rows == other._rows and self._columns == other._columns):
            temp = Mat([[0 for i in range(self._columns)] for _ in range(self._rows)])
            for i in range(self._rows):
                for j in range(self._columns):
                    temp[i,j] = self[i,j] * other[i,j]
            return temp
        else:
            raise ValueError("Matrices must be of the same dimensions")
    
    def __matmul__(self, other):
        if (self._columns == other._rows):
            temp = Mat([[0 for i in range(other._columns)] for _ in range(self._rows)])
            for i in range(self._rows):
                for j in range(other._columns):
                    sum = 0
                    for m in  range(other._rows):
                            sum += self[i,m] * other[m,j]
                    temp[i,j] = sum
            return temp
        else:
            raise ValueError("Rows of Matrix A must match columns of Matrix B")

    def __str__(self):
        output = ""
        for i in range(self._rows):
            output += "["
            for j in range(self._columns):
                output += f"{self[i,j]} "
            output = output[:-1] + "]\n"
        return output

    def __getitem__(self,indices):
        return self._data[indices[0]][indices[1]]
    
    def __setitem__(self,indices,value):
        self._data[indices[0]][indices[1]] = value
            


        

class Matrix:
    def __init__(self,rows = None,cols = None, data = None):
        if data is None:
            self._data = [[0 for _ in range(rows)] for _ in range(cols)]
            self._rows = rows
            self._cols = cols
        else:
            self._data = data
            self._rows = len(self._data[0])
            self._cols = len(self._data)
        
    @classmethod
    def str(cls,strMultiline):
        Datastr = strMultiline.split("\n")
        data = []
        for i in range(1,len(Datastr)-1):
            temp = list(map(int,Datastr[i].replace("[",'').replace("]",'').split(",")))
            data.append(temp)
        
        _rows = len(data[0])
        _cols = len(data)
        _data = [[0 for _ in range(_rows)] for _ in range(_cols)]
        for i in range(_rows):
            for j in range(_cols):
                _data[i][j] = data[i][j]
        print(f"{_data = }")
        return cls(_rows, _cols,_data)
        
    
    def __getitem__(self,indices):
        i,j = indices
        return self._data[i][j] 

    def __setitem__(self,indices,value):
        i,j = indices
        self._data[i][j] = value

    def __add__(self,other):
        if self._rows == other._rows and self._cols == other._cols:
            matReturn = Matrix(self._rows,self._cols)
            for i in range(self._rows):
                for j in range(self._cols):
                    matReturn[i,j] = self[i,j] + other[i,j]
        return matReturn
    
    def __sub__(self,other):
        if self._rows == other._rows and self._cols == other._cols:
            matReturn = Matrix(self._rows,self._cols)
            for i in range(self._rows):
                for j in range(self._cols):
                    matReturn[i,j] = self[i,j] - other[i,j]
        return matReturn
    
    def __str__(self):
        string = ""
        for i in range(self._rows):
            string += "["
            for j in range(self._cols):
                string += f"{self[i,j]},"
            
            string = string[:-1]+"]\n"
        return string

matA = Matrix.str("""
[1,0,0]
[0,1,1]
[0,1,1]
"""
)
matB = Matrix.str("""
[2,1,0]
[2,2,3]
[2,4,5]
""")

matC = matA - matB
print(matC)

matD = Mat([[1,2,4],[3,4,5]])
matE = Mat([[1,2,4],[3,4,5],[2,1,3]])
matF = matD @ matE
print(matF)
