import random, math

ls1 = [random.randrange(0, 100) for i in range(5)]
v2 = random.random()
print(ls1, v2)
vMax = max(ls1)
fd = vMax // v2
fact = math.factorial(fd)
print(vMax, fd, fact)