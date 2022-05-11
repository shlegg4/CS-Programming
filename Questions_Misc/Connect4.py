

class Stack:
    def __init__(self, len):
        self._len = len
        self._topPNTR = 0
        self._data = [None for _ in range(len)]

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def Append(self, item):
        self._data[self._topPNTR] = item
        self._topPNTR += 1


class Matrix:
    def __init__(self, rows, cols, data=None):
        if data is None:
            self._data = [Stack(rows) for _ in range(cols)]
        else:
            self._data = data
        self._rows = rows
        self._cols = cols

    @classmethod
    def str(cls, strMultiline):
        Datastr = strMultiline.split("\n")
        data = []
        for i in range(1, len(Datastr)-1):
            temp = list(map(int, Datastr[i].replace(
                "[", '').replace("]", '').split(",")))
            data.append(temp)

        _rows = len(data[0])
        _cols = len(data)
        _data = [Stack(_rows) for _ in range(_cols)]
        for i in range(_rows):
            for j in range(_cols):
                _data[j][i] = data[j][i]
        print(f"{_data = }")
        return cls(_rows, _cols, _data)

    def __setitem__(self, indices, value):
        i, j = indices
        self._data[i][j] = value

    def __getitem__(self, indices):
        i, j = indices
        return self._data[i][j]

    def convolution(func, filter, mat):
        matReturn = Matrix(mat._rows, mat._cols)
        for i in range(mat._rows - filter._rows+1):
            for j in range(mat._cols - filter._cols):
                for m in range(filter._rows):
                    for k in range(filter._cols):
                        matReturn[i+m, j+k] = func(mat[i+m, j+k], filter[m, k])
        return matReturn


def Multiply(a, b):
    return a * b


def main():
    #grid = Matrix(10,10)
    filterCross = Matrix.str("""
    [1,0,0,1]
    [0,1,1,0]
    [0,1,1,0]
    [1,0,0,1]
    """
                             )
    filterHORI = Matrix.str("""
    [1,1,1,1]
    """)
    filterVERT = Matrix.str("""
    [1]
    [1]
    [1]
    [1]
    """)

    matc = Matrix.convolution(Multiply, filterHORI, filterCross)
    print("")


matA = """
[1,0,0]
[1,1,0]
[1,0,1]
"""
matA = Matrix.str(matA)

main()
