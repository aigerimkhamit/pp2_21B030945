n = int(input())
a = []
for i in range(n):
    k = input()
    if(any(x.islower() for x in k) and any(x.isdigit() for x in k) and any(x.isupper() for x in k)):
        a.append(k)
a = set(a)
a = list(a)
a.sort()
print(len(a))
for x in a:
    print(x)