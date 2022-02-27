def mygen(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a = int(input())
for i in mygen(a):
    print(i)