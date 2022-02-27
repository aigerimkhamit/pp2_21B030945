class Shape:
    S = 0
    def area(self):
        print(f'{self.length * self.width}')

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        print(f'{self.length * self.width}')

s = Rectangle(6, 7)
s.area()