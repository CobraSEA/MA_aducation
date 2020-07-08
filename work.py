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
import string
'''
s = {'1':'a', '2':'b'}
print(id(s))
s = {'small ' + x: y for x, y in s.items()}
print(id(s))
print(s)
'''

str_l = "1q2w3e1q2w3re"
str_l = set(str_l)
str_p = set(list(string.punctuation))
print(str_p)
print(str_l)
print(bool(str_l & str_p))

STR_P = set(list("string"))
print(STR_P)
STR_P = {x for x in "string"}
print(STR_P)