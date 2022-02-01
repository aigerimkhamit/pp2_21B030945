distance, cart = input().split()

prime = True # булеан переменная 

x = range(2, int(distance) // 2 + 1) 
for n in x:
    if int(distance) % n == 0:
        prime = False 
        # тут мы проверяем числа на простоту

if int(distance) < 500 and prime == True and int(cart) % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")