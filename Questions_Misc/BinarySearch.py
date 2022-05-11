
Number = [10,9,9,8]


def FindName(s):
    Index = -1
    first = 0
    last = 14
    while last >= first and Index == -1:
        Middle = (first+last)//2
        if Number[Middle] == s:
            Index = Middle
        else:
            if Number[Middle] > s:
                last = Middle + 1
            else:
                first = Middle -1
    return Index

print(FindName(3))