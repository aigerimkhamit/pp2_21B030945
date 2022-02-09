n = int(input())
a = []
ans = []
for i in range(n):
    k = input().split()
    if k[0] == "1":
        a.append(k[1])
    else:
        ans.append(a[0])
        a.pop(0)
for i in ans:
    print(i, end = " ")