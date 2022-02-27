class Shape:
    S = 0
    def area(self):
        print(f'{self.length ** 2}')
class Square(Shape):
    def __init__(self, l):
        self.length = l
    def area(self):
        print(f'{self.length ** 2}')

s = Square(int(input()))
s.area()
    
