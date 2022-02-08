n = int(input())
a = []
cnt = 0
for i in range(n):
    k = input()
    if k == 1:
        d = input()
    else:
        d = " "
    if k == 2:
       cnt += 1
for i in range(n):
    if cnt != 0:
        for i in range(cnt):
            a.append(d)
print(a)
