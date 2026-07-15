class Turtle(object):

   def __init__(self, x, y, s ):
        self.x = x
        self.y = y
        self.s = s
    
   def go_up(self):
        self.y += self.s

   def go_down(self):
        self.y -= self.s

   def go_left(self):
        self.x -= self.s

   def go_right(self):
        self.x += self.s

   def evolve(self):
        self.s += 1

   def degrade(self):
        if (self.s -1) <= 0:
            print(f"Невозможно уменьшить s")
        else:
            self.s -= 1

   def count_moves(self, x2, y2):
        xs = abs(x2- self.x)
        ys = abs(y2- self.y)
        if (xs % self.s) !=0 or (ys % self.s) !=0:
             print(f"С данным шагом невозможно встать на заданную позицию")
        else:
            total= (xs+ys)/self.s
            print(f"Минимальное количество действий чтобы добраться до указанных координат: {int(total)}")


 