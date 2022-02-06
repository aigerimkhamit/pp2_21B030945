k = int(input())
b = [[0 for i in range(k)] for j in range(k)]

for i in range(k):
    for j in range(k):
        if i == j:
            b[i][j] = i * j
        else:
            b[i][j] = 0

for i in range(k):
    b[0][i] = i
for i in range(k):
    b[i][0] = i

for i in range(k):
    for j in range(k):
        print(b[i][j], end = " ")
    print()
