from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def get_square_c(self):
        pass
    @abstractmethod
    def get_square_s(self):
        pass
    @abstractmethod
    def get_sq_full(self):
        pass

class Material(MyAbstractClass):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self): #расход ткани для пальто
        return (self.width / 6.5 + 0.5)

    def get_square_s(self):
        return (self.height * 2 + 0.3) #расход ткани для пальто

    @property
    def get_sq_full(self):  #общий расход ткани
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c}'


class Suit(Material):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_s}'

coat = Coat(5, 11)
suit = Suit(5, 10)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
