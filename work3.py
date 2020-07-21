import time
from functools import reduce
from math import factorial
from operator import mul, truediv

SEC = 1
def printer(func):
    call_counter = 0
    def wrapped(*args, **kwargs):
        nonlocal call_counter
        ctime = time.time()
        result = func(*args, **kwargs)
        #print(f'Execution time = {time.time() - ctime - SEC}')
        call_counter += 1
        print(f'in wrapped, call_counter = {call_counter}')
        return result
    return wrapped


@printer
def some():
    time.sleep(SEC)
    return 1

@printer
def next_some():
    return 2

def make_averager():
    lst = []
    def aver(value: int = None) -> object:
        if value is not None:
            lst.append(int(value))
            v = int(sum(lst) / len(lst))
            print(v)
            return v
        else:
            print('No params in call!')
            return 0
    return aver

avg = make_averager()


def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def fact1(n):
    return reduce(mul, range(1, n + 1))

print(fact(4))
print(fact1(5))
print(factorial(4))
