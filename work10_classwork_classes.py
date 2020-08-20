class Car:
    __cars = 0
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self._engine = 'F4N6'
        Car.__cars += 1
        print(f'Obj {self.__class__.__name__} was created')
        print(f'Created {Car.__cars} cars')

    def get_info(self):
        return self.__dict__

    def change_engine(self, engine):
        self._engine = engine
        return self._engine

    @property
    def engine(self):
        return self._engine

    @engine.deleter
    def engine(self):
        if type(self) == Car:
            print(f'Can`t delete engine of {self.__class__.__name__}')
        else:
            del self._engine
            print(f'{self.__class__.__name__} was deleted')

    def obj_info(self):
        print(self)
        print(isinstance(self, Car))
        print(isinstance(self, Sportcar))


class Sportcar(Car):
    def __init__(self, name, model, color):
        super().__init__(name, model)
        self.color = color

    def change_color(self, color):
        self.color = color
        return self.color

    def get_info(self):
        return self.__dict__

armada = Car('Nissan', 'Armada')
mustang = Sportcar('Ford', 'Mustang', 'Red')

#mustang.obj_info()
#armada.obj_info()

print(mustang.name)
print(armada.get_info())
print(mustang.get_info())
mustang.change_color('Yellow')
print(mustang.get_info())
print(mustang.engine)
del mustang.engine
del armada.engine
print(armada.get_info())
print(mustang.get_info())
#print(armada.engine)
#print(mustang.engine)

