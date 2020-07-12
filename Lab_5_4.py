foo = [1, 2, 3, 4, 5]
odd_foo = []

def isOdd(x):
    return x % 2 == 1

for f in foo:
    if isOdd(f):
        odd_foo.append(f)
print (odd_foo)

print([i for i in range(1, 6) if (lambda x: x % 2 == 1)(i)])
print([i for i in range(1, 6) if i % 2 == 1])