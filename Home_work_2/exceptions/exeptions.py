class ValueErrorEx(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Скорость ветра {wind}.Слишком мало для паруса'