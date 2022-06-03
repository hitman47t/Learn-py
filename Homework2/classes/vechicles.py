from exceptions.exeptions import ValueErrorEx

class Vechicle:

    def __init__(self, weight = 1500, speed = 200):
        self.name = ''
        self.weight = weight
        self.speed = speed
        self.sound = 'default'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name} {self.speed},{self.weight})'

    def get_sound(self):
        return self.sound

    def rename(self, new_name:str):
        self.name = new_name


class Boat(Vechicle):

    def __init__(self, weight=200, speed = 60, displacement = 1500):
        self.name = 'Boat'
        self.weight = weight
        self.speed = speed
        self.sound = 'Choooooooooo-chooooo'
        self.displacement = displacement

    def __repr__(self):
        return Vechicle.__repr__(self) + f'(displacement = {str(self.displacement)})'

class Car(Vechicle):

    def __init__(self, weight, speed, wheels=4):
        self.name = 'Car'
        self.weight = weight
        self.speed = speed
        self.sound = 'Beep'
        self.wheels = wheels

    def __repr__(self):
        return Vechicle.__repr__(self) + f'(wheels = {str(self.wheels)})'

class Helicopter(Vechicle):

    def __init__(self, weight=1200, speed = 250, altitude = 2500):
        self.name = 'Helicopter'
        self.weight = weight
        self.speed = speed
        self.sound = 'Hrhrhrhrhrrrhrhrhr'
        self.altitude = altitude

    def __repr__(self):
        return Vechicle.__repr__(self) + f'(altitude = {str(self.altitude)})'


class SailBoat(Boat):

    def spread_the_sail(self, wind=5):

        # try:
            if wind >= 5:
                return f'Скорость ветра {wind}.Парус развернут'
            else:
                raise ValueErrorEx(wind)
        # except:
        #     return f'Скорость ветра {wind}.Слишком мало для паруса'
