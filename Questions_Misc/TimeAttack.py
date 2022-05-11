import time

class Database:
    def __init__(self):
        self._Password = "13453020"
        self._Data = "MWAHHAHAA"
    
    def Access(self, Password):
        if Password == self._Password:
            return self._Data
        else:
            return None

database = Database()



for _ in range(10):
    time.sleep(1)
    Guess = "13000000"
    start = time.perf_counter_ns()
    if Guess == "13453020":
        print("Correct guess")
    end = time.perf_counter_ns()
    elapsed = end - start
    print(f"{elapsed = } nanoseconds")
    print(f"{end = }, {start = }")
    
    time.sleep(1)
    Guess = "13000000"
    start2 = time.perf_counter_ns()
    if Guess == "13453020":
        print("Correct guess")
    end2 = time.perf_counter_ns()
    elapsed2 = end2 - start2
    print(f"{elapsed2 = } nanoseconds")
    print(f"{end2 = }, {start2 = } \n")

