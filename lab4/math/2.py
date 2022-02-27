class Trapezoid:
    S = 0
    def area(self):
        print(f'{((self.a + self.b)* self.height) / 2}')
class Square(Trapezoid):
    def __init__(self, h, a, b):
        self.height = h
        self.a = a
        self.b = b
    def area(self):
        print(f'{((self.a + self.b)* self.height) / 2}')

a = Square(5, 5, 6)
a.area()