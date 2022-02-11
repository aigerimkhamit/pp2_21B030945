a = []
while True:
    d = input()
    if d == "0":
        break
    a.append(d.split())
a.sort(key = lambda x:(x[2], x[1], x[0]))
for i in a:
    for j in i:
        print(j, end = " ")
    print()