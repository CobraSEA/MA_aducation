# print("15.5".isdigit(), "15".isdigit())
"""
try:
   t = "2000:2020"
   t = t.replace(":",",")
   r = t.split(",")
   g1, g2 = [int(q) for q in r]
   print(r, type(g1), g2)
except ZeroDivisionError as r:
    print(r.args)
"""
'''
s = {'1':'a', '2':'b'}
print(id(s))
s = {'small ' + x: y for x, y in s.items()}
print(id(s))
print(s)

str_l = "1q2w3e1q2w3re"
str_l = set(str_l)
str_p = set(list(string.punctuation))
print(str_p)
print(str_l)
print(bool(str_l & str_p))

import getpass
password = getpass.getpass("Enter pass:")
print(password)
password = 'sdsds'
#STR_P = set(list("string"))
#print(STR_P)
#STR_P = {x for x in "string"}
#print(STR_P)
#STR_P = set("string")
#print(STR_P)


def spam():
    cnt = 0
    while True:
        yield cnt
        cnt += 1
reg = spam()
for x in range(10):
    print(next(reg), end=' ')

a = {'a':1, 'b':2}
b = [6, 7, 8, 'Yes', 'No']
L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L:
    print(f(2))
    print(L[0](3))

def fib(n):
    a, b = 0, 1
    for f in range(1, n):
        if f == 1:
            yield a
        yield b
        a, b = b, a + b

t = fib(10)
for i in t:
    print(i)
'''

L = [2, 4, 6, 8]
D = [1, 3, 6, 8]

def l_add(a, b=0, lst=[]):
    if lst:
        a.extend(lst)
    else:
        a.append(b)
    return(a)

print(L)
print(l_add(L, lst=[1, 3, 5, 7]))
print(l_add(L, 10))
