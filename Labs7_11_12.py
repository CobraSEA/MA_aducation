class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self._number = number

        if number < 0:
            self.place = 'out of stock'
        elif number < 100:
            self.place = 'warehouse'
        else:
            self.place = 'Remote warehouse'

class Building2:

    @staticmethod
    def _set_place(number):
        if number < 0:
            return 'out of stock'
        elif number < 100:
            return 'warehouse'
        else:
            return 'Remote warehouse'

    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self._number = number
        self.place = self._set_place(number)

    def plus(self, number):
        self._number += number
        self.place = self._set_place(number)

    def minus(self, number):
        self._number -= number
        self.place = self._set_place(number)

    def __str__(self):
        return f'\n Obj {self.__class__.__name__} ' \
               f'material: {self.material}, color: {self.color}, ' \
               f'number: {self._number}, place: {self.place}'


if __name__ == '__main__':
    a = Building('shifer', 'Yellow', 600)
    print(a)

    b1 = Building2('brick', 'white', 60)
    b2 = Building2('plank', 'brown', 20)
    print(b1, b2)
    b1.plus(50)
    b2.minus(3)
    print(b1, b2)