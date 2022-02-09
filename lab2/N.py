b = []
while True:
    a = int(input())
    if a == 0:
        break
    b.append(a)

if len(b) % 2 == 0:
    x = len(b) // 2
    for i in range(x):
        print(b[0] + b[-1], end = " ")
        b.pop(0)
        b.pop()
else:
    y = (len(b) // 2)
    for i in range(y):
        print(b[0] + b[-1], end = " ")
        b.pop(0)
        b.pop()
        if(len(b) == 1):
            print(b[len(b) // 2])