import math
def square(n, l):
    return(n * (l ** 2)) / (4 * (math.tan(math.pi / n)))
n = int(input())
l = int(input())
print(round(square(n, l)))