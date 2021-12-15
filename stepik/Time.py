import time

def one(a, b, c):
    return a + b + c

def two(*args):
    return args[0] + args[1] + args[2]

count = 9000000
_startTime = time.time()
for num in range(count):
    one(1, 2, 3)
print("Positional test:", time.time() - _startTime)

_startTime = time.time()
for num in range(count):
    two(1, 2, 3)
print("Positional args as list test:", time.time() - _startTime)
