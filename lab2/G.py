n = int(input())
a = {}

for i in range(n):
    d, w = input().split()
    if w in a:
        a[w] += 1
    else:
        a[w] = 1

m = int(input())
b = {}

for i in range(m):
    q, r, t = input().split()
    t = int(t)
    if r in b:
        b[r] += t
    else:
        b[r] = t

cnt = 0
for i in a:
    if i in b:
        if a[i] > b[i]:
            cnt += a[i] - b[i]
    else:
        cnt += a[i]
print("Demons left:", cnt)
