from Labs7_11_12 import *
import math
class Market(Building2):  # for lab 7.22
    def __init__(self, material, color, number, price):
        super().__init__(material, color, number)
        self.price = price


class Market2(Building2):  # for lab 7.23

    def plus(self, number):
        super().plus(number / 2)

    def minus(self, number):
        super().minus(number / 2)


a1 = Building2('Brick', 'Yellow', 200)
a2 = Building2('Plank', 'Red', 10)
m1 = Market('Brick', 'white', 70, 300)
m2 = Market2('Brick', 'green', 110)
print(a1, a2, m1, m2)
a1.plus(1)
a2.minus(2)
m1.plus(40)
m2.minus(50)
print(a1, a2, m1, m2)
print(a1.number)
