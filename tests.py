"""
str1 = 'sdsdsds'
try:
    for i in "123":
        print(i)

except ZeroDivisionError:
    print("div by zero")
except IOError:
    print("IOError")
except RuntimeError:
    print("RuntimeError")
finally:
    print("fin block")
"""
string = "one simple string"
string2 = string
#print(id(string), " ", id(string2))
string2 = string + " PPP"
print(f"String = {string} id = {id(string)}; string2 = {string2} id = {id(string2)}")
#dict = {"sss":1, "ss":2}

#try:
#    raise RuntimeError('runtimeerror')
#except Exception:
#    print("except exception")
#except RuntimeError:
#    print('except runtime error')
"""
def fun():
    x = 1
    while False:
        return 0


for i in None:
    print('s')
"""