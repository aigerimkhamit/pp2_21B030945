a = int(input())
x = list(map(int, input().split()))
x.sort(reverse = True)
print(int(x[0]) * int(x[1]))