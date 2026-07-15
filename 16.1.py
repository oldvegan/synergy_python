class Kassa(object):

   def __init__(self, money):
        self.money = money
    
   def top_up(self, x):
        self.money += x
    
   def count_1000(self):
       print(f"Целых тысяч в кассе имеется: {self.money // 1000}")

   def take_away(self, x):
       if x <= self.money:
           self.money -= x
       else:
           print(f"В кассе денег меньше, чем вы запросили")
           

kassa = Kassa(1000)
kassa.top_up(1500)
print(kassa.money)
kassa.count_1000()
kassa.take_away(2000)
print(kassa.money)
kassa.take_away(501)
