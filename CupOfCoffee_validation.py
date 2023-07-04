""" Rласс CupOfCoffee, c атрибутjv size_ml и свойствjv filled_ml. Добаввлена валидация значения свойства filled_ml: оно не должно превышать значение атрибута size_ml и быть меньше 0. Используйте при валидации созданные ранее классы исключений.
Создана внешняя функцию, которая заполняет значение свойства filled_ml и обрабатывает исключения."""

from validationError import TooSmallValue, TooBigValue

class CupOfCoffee:
    def __init__(self, size_ml, filled_ml):
        self.size_ml = size_ml
        self.filled_ml = filled_ml

        # Validation for the filled_ml value
        if self.filled_ml > self.size_ml:
            raise TooBigValue(self.size_ml, 'Слишком много кофе')
        elif self.filled_ml < 0:
            raise TooSmallValue(0, 'Объем кофе не может быть отрицательным!')


def fill_cup_of_coffee(cup, ml):
    try:
        #ml += 100
        cup.filled_ml = ml
    except TooSmallValue as error:
        print('Ошибка заполнения:', error)
    except TooBigValue as error:
        print('Ошибка заполнения:', error)


cup = CupOfCoffee(200, 150)
ml = 250

result = fill_cup_of_coffee(cup, ml)
print(result)
