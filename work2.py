import functools
def dec_prn_name(func):
    print(func)
    def his_add(name, sname='Connor'):
        print(name)
        return f'His {func(name, sname)}'
    return his_add

def dec2_prn_name(func):
    def capit(name, sname='Connor'):
        return func(name.capitalize(), sname.capitalize())
    return capit

@dec2_prn_name
@dec_prn_name
def print_name(name, sname='Connor'):
    print(sname)
    return "name is " + name + ' ' + sname

#dec_func = dec_prn_name(print_name)
print(print_name("john"))

def do(x, y):
    return x * y

def red(func, coll):
    L = coll[0]
    for i in coll[1:]:
        L = func(L, i)
    return L

s = [1,2,3,4]
print(functools.reduce(do, s))
print(red(do, s))
#print(list(map(do, s)))

#x = 4
def ff():
    pass
print(ff())
print(print())

