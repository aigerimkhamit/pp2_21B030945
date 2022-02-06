n = int(input())
str = "@gmail.com"
for i in range(n):
    i = input()
    x =  i.endswith(str)
    if x == True:
        c = i.find(str)
        print(i[:c]) # slicing string, printing the part we need
        