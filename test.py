from exceptions import TooSmallValue, TooBigValue

class CupOfCoffeeDescriptor:

    def __init__(self):
        self.__value = None

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if value > instance.size_ml:
            raise TooBigValue(instance.size_ml, 'filled_ml is too big!')
        elif value < 0:
            raise TooSmallValue(0, 'filled_ml cannot be negative!')
        else:
            self.__value = value


class CupOfCoffee:
    filled_ml = CupOfCoffeeDescriptor()

    def __init__(self, size_ml):
        self.size_ml = size_ml



def fill_cup_of_coffee(cup, ml):
    try:
        cup.filled_ml = ml
    except TooSmallValue as error:
        print('Filling error:', error)
    except TooBigValue as error:
        print('Filling error:', error)
