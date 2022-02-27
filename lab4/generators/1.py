def mygen(n):
    for i in range(n):
        yield i ** 2
for i in mygen(10):
    print(i)