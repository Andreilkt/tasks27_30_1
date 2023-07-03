from validationError import TooSmallValue, TooBigValue

class CupOfCoffee:
    def __init__(self, size_ml, filled_ml):
        self.size_ml = size_ml
        self.filled_ml = filled_ml

        # Validation for the filled_ml value
        if self.filled_ml > self.size_ml:
            raise TooBigValue(self.size_ml, 'filled_ml is too big!')
        elif self.filled_ml < 0:
            raise TooSmallValue(0, 'filled_ml cannot be negative!')


def fill_cup_of_coffee(cup, ml):
    try:
        cup.filled_ml = ml
    except TooSmallValue as error:
        print('Filling error:', error)
    except TooBigValue as error:
        print('Filling error:', error)
        

