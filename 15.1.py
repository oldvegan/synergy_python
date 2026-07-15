class Transport(object):

   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

autobus = Transport("Renaul Logan", 180, 12)


print(f"Название автомобиля: {autobus.name}\n Скорость: {autobus.max_speed} км/ч \n Пробег: {autobus.mileage} км")