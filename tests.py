from functools import reduce
from operator import mul

a = [1, 2, 7, 8]
b = [3, 5, 4]

def pr_lst(a, b):
    for i in range(len(a)):
        if i >= len(b):
            print(a[i])
            break
        else:
            print(a[i] * b[i])

def ml_lst(a, b):
    return [a[i] * b[i] for i in range(len(a)) if i < len(b)]

pr_lst(a, b)
c = ml_lst(b, a)
print(c)

print(reduce(mul, a))

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('fooxX'))