s = input()
sum = 0 # вводим новую переменную, чтобы суммировать 

for i in s:
    sum += ord(i)

if int(sum) < 300:
    print("Oh, no!")
else:
    print("It is tasty!")