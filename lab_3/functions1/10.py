def set(list):
    a = []
    for i in list:
        if i not in a:
            a.append(i)
    for i in a:
        print(i, end = ' ')
a = input().split()
set(a)