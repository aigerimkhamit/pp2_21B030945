def mygen(n):
    i = n - 1
    while i != 0:
        yield i
        i -= 1
    else:
        yield 0
a = int(input())
for x in mygen(a):
    print(x)