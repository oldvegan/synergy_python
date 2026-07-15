class Transport(object):

   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

   def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"
    
class Autobus(Transport):
   def __init__(self, name, max_speed, mileage, capacity=50):
        super().__init__(name, max_speed, mileage)
        self._capacity = capacity
   def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}: {self._capacity} пассажиров"

autobus = Autobus("Renaul Logan", 120, 15000)
print(autobus.seating_capacity())

