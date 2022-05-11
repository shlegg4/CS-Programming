import time


A = "A"
Abin  =  A.encode("utf-8")
print(hash(Abin))
time.sleep(1)
print(hash(A))
