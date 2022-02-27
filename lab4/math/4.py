class parallelogram:
    def __init__(self, length, height):
        self.length = length
        self.height = height
    def area(self):
        print(f'{float(self.length * self.height)}')
a = parallelogram(5, 6)
a.area()