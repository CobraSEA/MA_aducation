from functools import partial
from functools import lru_cache
from collections import namedtuple
from typing import NamedTuple

def rec_fact(n):
    return n * rec_fact(n - 1) if n > 1 else n


def func_kw(**kwargs):
    for k, v in kwargs.items():
        print(f'Arg {k} = {v}')


def mult(x, y):
    return x * y

#func_kw(foo='bar', num=9)
#print(rec_fact(5))

def run(func):
    print(func())
f = partial(mult, 3)
#print(f(2))

cityes = namedtuple('City', 'contry square population')
#aircrafts = NamedTuple('aircarft', model=str, seats=int, range=int)
aircrafts = NamedTuple('aircarft', [('model', str), ('seats', int), ('range', int)])

Kyiv = cityes('Ukraine', 839, 3.4)
Lviv = cityes('Ukraine', 182, 0.724)

B738 = aircrafts(model='738', seats=189, range=2935)
B739er = aircrafts('739', 220, 2950)
"""
print(Kyiv, id(Kyiv), Kyiv.contry, *Kyiv)
print(Lviv)
print(Kyiv._asdict())
print(Kyiv._replace(square=0))
for ind, val in Lviv._asdict().items():
    print(f'{ind} = {val}')

print(B738)
print(B739er)
"""
def fibo_c(func):
    fib_list = {}
    def cash(n):
        result = func(n)
        if n not in fib_list.keys():
            fib_list.update({n: result})
            print(fib_list)
            return result
        else:
            print(f'Else {n}')
            return fib_list[n]
    return cash


@fibo_c
def fibo(n):
    return n if n < 2 else fibo(n - 2) + fibo(n - 1)


@lru_cache(maxsize=32)
def fibo_lru(n):
    return n if n < 2 else fibo_lru(n - 2) + fibo_lru(n - 1)

print(fibo(6))
print(fibo_lru(6))
print(fibo_lru.cache_info())