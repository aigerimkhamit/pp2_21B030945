k = int(input())
b = [[0 for i in range(k)] for j in range(k)]

if k % 2 == 0:
    for i in range(k):
        for j in range(k):
            if i == j or i > j:
                b[i][j] = "#"
            else:
                b[i][j] = "." 
else:
    for i in range(k):
        for j in range(k):
            if i + j == k - 1 or i + j > k - 1:
                b[i][j] = "#"
            else:
                b[i][j] = "."

for i in range(k):
    for j in range(k):
        print(b[i][j], end = "")
    print()
