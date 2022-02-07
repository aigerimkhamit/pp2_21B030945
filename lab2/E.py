n = list(map(int, input().split()))
if len(n) == 1:
    b = int(input())
    k = 0
    for i in range(n[0]):
        i = b + 2 * i
        k = k ^ i
    print(k)
else:
    cnt = 0
    for i in range(n[0]):
        i = n[1] + 2 * i
        cnt = cnt ^ i
    print(cnt)