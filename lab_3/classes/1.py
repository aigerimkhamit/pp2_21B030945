class Mine:
    def __init__(self):
        self.name = " "
    def get(self):
        self.name = input()
    def print(self):
        print(self.name.upper())

name = Mine()
name.get()
name.print()


