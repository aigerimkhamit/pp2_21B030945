x, y = map(int, input().split())
n = int(input())
import math
a = []
k = []

for i in range(n):
    key = input()
    a.append(key.split())
for i in a:
    p = math.sqrt(pow(int(i[0]) - x, 2) + pow(int(i[1]) - y, 2))
    k.append(p)
k.sort()
for i in k:
    for j in a:
        if i == math.sqrt(pow(int(j[0]) - x, 2) + pow(int(j[1]) - y, 2)):
            print(j[0], j[1])
            a.remove(j)