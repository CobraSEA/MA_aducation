class Pet:
    a = 5
    def __init__(self, name, pet_type, age):
        self.name = name
        self.__pet_type = pet_type
        self.age = age

    def rename(self, new_name):
        self.name = new_name
        return new_name

    def __gt__(self, other):
        if isinstance(other, Pet):
            return self.age > other.age
        raise NotImplemented


    def get_type(self):
        return self.__pet_type

a = Pet('Alex', 'cat', 10)
b = Pet('Sanek', 'dog', 3)

class Dog(Pet):
    #__color = None
    def __init__(self, name, pet_type, age, color):
        super().__init__(name, pet_type, age)
        self.__color = color

    def bark(self):
        print('bark!')

    def set_color(self, color):
        self.__color = color
        return color

    @property
    def color(self):
        return self.__color

dog = Dog('Gerom', 'Sharpey', 6, 'white')
print(dog.color)
dog.set_color('red')
print(dog.color)
print(dog.name, dog.get_type())
dog.bark()
dog.__color = 'yellow' # ignore command
print(dog.color)
print(dir(dog))
print(dog.color)