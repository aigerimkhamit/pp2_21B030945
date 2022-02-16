import math
def sphere(r):
    k = 4/3 * math.pi * r * r * r
    return k
r = int(input())
print(sphere(r))