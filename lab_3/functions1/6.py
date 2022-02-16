def rev(s):
    k = s[::-1]
    for i in k:
        print(i, end = ' ')

s = input().split(" ")
rev(s)