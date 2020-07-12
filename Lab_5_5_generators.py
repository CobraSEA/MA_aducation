ls = [x + 1 for x in range(5)]

def enumerator(lst):
    for l in lst:
        yield lst.index(l) + 1, l

for i in enumerator(ls):
    print(i)