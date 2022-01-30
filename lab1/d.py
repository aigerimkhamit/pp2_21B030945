num = input() # первое число
char = input() # чар, определяющий команду

num = int(num) # переводим в интеджер

from decimal import *
if char == "k":
    d = input()
    d = int(d)
    print(round(num / 1024, d))
elif char == "b":
    print(num * 1024)
