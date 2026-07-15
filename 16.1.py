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
