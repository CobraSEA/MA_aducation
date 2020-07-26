import sys
print(sys.platform)
print(sys.implementation.version)
print(sys.getsizeof("abc"))

n = 11
for arg in sys.argv[1:2]:
    n = int(arg)

for arg in sys.argv:
    if arg.isdigit():
        sys.stdout.write(arg + ' ')
        if int(arg) % 2 == 0:
            sys.exit(n)