import math
class Point():
    def __init__(self, x, y):
        #x - the value on the x-axis
        #y - the value on the y-axis
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
        #выводит значения 
    def move(self, x, y):
        self.x += x
        self.y += y   
        #меняем координаты точки   
    def dist(self, d):
        a = d.x - self.x
        b = d.y - self.y
        return math.sqrt(a ** 2 + b ** 2)
        #находим дистанцию между двумя точками

a = Point(2,3)
b = Point(4,5)
a.move(7, 10)
print(a.show())
print(a.dist(b))
