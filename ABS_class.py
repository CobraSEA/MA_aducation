from abc import abstractmethod, ABC


class Dogs(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'{self.__class__.__name__}: name = {self.name}, age = {self.age}')

    @abstractmethod
    def bark(self):
        raise NotImplementedError(f'Need to implement bark')

    @abstractmethod
    def play(self):
        pass


class Pug(Dogs):
    def bark(self):
        print(f'{self.__class__.__name__} {self.name}: tyaf-tyaf-tyaf!')

    def play(self):
        print(f'{self.__class__.__name__} {self.name}: is playing with ball!')


class Mastiff(Dogs):
    def bark(self):
        print(f'{self.__class__.__name__} {self.name}: Wooooofff!')

    def play(self):
        print(f'{self.__class__.__name__} {self.name}: is playing with his tail!')


class Taksa(Dogs):
    """empty class"""


dog1 = Pug('Piggi', 7)
dog2 = Mastiff('John', 2)
# dog3 = Taksa('Jeeny', 4)

dog1.bark()
dog2.bark()
# dog3.bark()
dog1.play()
dog2.play()
# dog3.play()
dog1.get_info()
dog2.get_info()
# dog3.get_info()
