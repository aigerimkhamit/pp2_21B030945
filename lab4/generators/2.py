cnt = []
def mygen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
a = int(input())
for i in mygen(a):
    cnt.append(str(i))
print(','.join(cnt))