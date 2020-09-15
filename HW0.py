from abc import abstractmethod, ABC
from functools import total_ordering
from random import randrange


class Father(ABC):
    __slots__ = ('lst',)

    def __init__(self, lst):
        self.lst = lst

    @abstractmethod
    def load(self, lst):
        pass

    @abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.lst)

    def inspect(self):
        return tuple(sorted(self.lst))

    def __str__(self):
        return str(self.lst)


class Child(Father):

    def load(self, lst):
        self.lst += lst

    def pick(self):
        i = randrange(len(self.lst))
        if i > 0:
            return self.lst.pop(i)

    def __getitem__(self, item):
        return self.lst[item]

    def __contains__(self, item):
        return item in self.lst

    def __mul__(self, other):
        # return [i * other for i in self.lst]
        def _ml_lst(a, b):
            ls = []
            for i in range(len(a)):
                if i >= len(b):
                    ls.append(a[i])
                else:
                    ls.append(a[i] * b[i])
            return ls

        if isinstance(other, Father):
            return Child(_ml_lst(self.lst, other.lst))
        if isinstance(other, (list, tuple, set)):
            return _ml_lst(self.lst, list(other))
        if isinstance(other, (int, float)):
            return [i * other for i in self.lst]

    def __add__(self, other):
       # print('work __add__')
        if isinstance(other, Father):
            return Child(self.lst + list(other.lst))
        if isinstance(other, (list, tuple, set)):
            return self.lst + list(other)
        if isinstance(other, (int, float, str)):
            return self.lst + [other]

    def __radd__(self, other):
        # print('work __radd__')
        if isinstance(other, Father):
            return Child(self.lst + list(other.lst))
        if isinstance(other, (list, tuple, set)):
            return self.lst + list(other)
        if isinstance(other, (int, float, str)):
            return self.lst + [other]

    def __sub__(self, other):
        if isinstance(other, Father):
            return [i for i in self.lst if i not in other.lst]
        if isinstance(other, (list, tuple, set)):
            return [i for i in self.lst if i not in list(other)]
        if isinstance(other, (int, float, str)):
            self.lst.remove(other)
            return self.lst

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return [i / other for i in self.lst if other != 0]

    def __mod__(self, other):
        return [i % other for i in self.lst if other != 0]

@total_ordering
class NoChange(Father):  # __slots__
    __slots__ = ('lst', )

    def __init__(self, tup):
        super().__init__(tup)
        self.lst = tuple(tup)

    def __str__(self):
        return str(self.lst)

    def __eq__(self, other):
        return sum(self.lst) == sum(other.lst)

    def __lt__(self, other):
        return sum(self.lst) < sum(other.lst)

    def load(self, lst):
        self.lst += tuple(lst)

    def pick(self):
        return self.lst.index(randrange(len(self.lst)))

    def __add__(self, other):
       # print('work __add__')
        if isinstance(other, Father):
            return Child(self.lst + tuple(other.lst))
        if isinstance(other, (list, tuple, set)):
            return self.lst + tuple(other)
        if isinstance(other, (int, float, str)):
            return self.lst + (other, )


c0 = Child([3, 7, 9])
c1 = Child([9, 2])
c2 = NoChange([5])
c3 = NoChange([3, 2])
#  c1.load([2, 3, 4, 5])
c3.load([0, 5, 9, 3])

print(f'c0 = {c0}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')
print(f'c3 = {c3}')
print(c3 < c2)
print(c3 >= c2)
print(c3 == c2)
print(f'pick = {c0.pick()}')
print(f'c0.loaded() = {c0.loaded()}')
c0.load([66, 105, 12])
print(f'inspect c0 = {c0.inspect()}')
print(f'c0 = {c0}')
print(f'c0[:2] = {c0[:2]}')  # __getitem__
print(f'5 in c0 = {5 in c0}')  # __contains__
print(f'c0 * 3  = {c0 * 3}')  # __mul__
print(f'c0 + 2  = {c0 + 2}')  # __add__

#  __add__ sectinon
c3 = c0 + c1
print(f'c3 = c0 + c1 = {c3} ret type = {type(c3)}')
print(f'c0 + [12, 15] = {c0 + [12, 15]} ret type = {type(c0 + [12, 15])}')
print(f'c0 + (13, 14) = {c0 + (13, 14)} ret type = {type(c0 + (13, 14))}')
print(f'c0 + 17 = {c0 + 17} ret type = {type(c0 + 17)}')
print(f'c0 + 12.1 = {c0 + 12.1} ret type = {type(c0 + 12.1)}')
print(f'c0 + "string" = {c0 + "string"} ret type = {type(c0 + "string")}')
print(f'c0 + c2 = {c0 + c2} ret type = {type(c0 + c2)}')
c3 += c3
print(f'c3 += c3: {c3} ret type = {type(c3)}')
print(f'17 + c0 = {17 + c0} ret type = {type(17 + c0)}')

# __mul__ sectinon
print(c1, c0)
print(f'c1 * c0  = {c1 * c0}')
print(f'c0 * c1  = {c0 * c1}')
print(f'c0 * 2.5  = {c0 * 2.5}')

# __sub__ section
print(f'c0 - c1  = {c0 - c1}')
print(f'c0 - 3  = {c0 - 3}')
print(f'c0 - (9, 5)  = {c0 - (9, 5)}')

print(f'c2 + 2  = {c2 + 2}')  # __add__
print(f'c2 = {c2}')  # __add__
print(f'c0 % 3  = {c0 % 3}')  # __mod__
print(f'c0 / 3  = {c0 / 3}')  # __truediv__

#for t in c0: # can iterate by __getitem__
#    print(t)