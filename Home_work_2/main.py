from classes import vechicles, fuel
from Utils import getSpeed


boat = vechicles.Boat(500, 100, 20)
print(boat)

helic = vechicles.Helicopter()
print(helic)

car = vechicles.Car(2000, 220, 4)
print(car)

#Вывод звуков транс. средств
print()
print(boat.get_sound())
print(helic.get_sound())
print(car.get_sound())

# Использование метода переименования
print()
car.rename('Lambo')
print(car)

print()
# sailboat = vechicles.SailBoat()
# sailboat.rename('SuperBoat')
# print(sailboat)
# print(sailboat.get_sound())
# print(sailboat.spread_the_sail(wind=4))

# Использование датакласса Fuel
benzin = fuel.Fuel('Benz', 'Euro95')
print(benzin, benzin.name, benzin.octane)
print()

# Использование ф-ции с exception
print('Speed = ', getSpeed(0,200))