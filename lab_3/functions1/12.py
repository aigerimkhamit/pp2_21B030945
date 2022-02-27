def histogram(list):
    for i in list:
        for x in range(i):
            print("*", end = '')
        print()

a = list(map(int, input().split()))
histogram(a)