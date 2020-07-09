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
'''

def spam():
    cnt = 0
    while True:
        yield cnt
        cnt += 1
reg = spam()
for x in range(10):
    print(next(reg), end=' ')
