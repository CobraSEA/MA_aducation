from math import hypot

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return (self.x, self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __iter__(self):
        return iter((self.x, self.y))

    def __abs__(self):
        return hypot(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


v1 = Vector(10, 30)
v2 = Vector(10, 30)
print(v1())
print(v1)
x, y = v1
print(x, y)
print(abs(v1))
print(v1 == v2)
s1 = {v1, v2}
print(s1)
