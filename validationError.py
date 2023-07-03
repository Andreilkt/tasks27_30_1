""" Класс создает исключение,  наследуется о класса ValueError. """

# создание родителььского класса ValidationError
class ValidationError(ValueError):

    # конструктор класса ValidationError, обращение к конструктору родительского класса
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    # Метод возвращяет сообщение
    def __str__(self):
        return self.message

# Создание классов наследников от класса ValidationError
class TooSmallValue(ValidationError):
    def __init__(self, message):
        super().__init__(message)

class TooBigValue(ValidationError):
    def __init__(self, message):
        super().__init__(message)

# Функция validate_value, использует созданные ранее исключения
def validate_value(value):
    if value < 0:
        raise TooSmallValue("Значение должно быть больше или равно 0.")
    if value > 100:
        raise TooBigValue("Значение должно быть меньше или равно 100.")

# Вызов функции validate_value

try:
    validate_value(101)
except TooSmallValue as e:
    print("Cлишком маленькое значение:", str(e))
except TooBigValue as e:
    print("Cлишком большое значение:", str(e))
except ValidationError as e:
    print("Ошибка проверки:", str(e))
