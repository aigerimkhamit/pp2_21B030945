import math
def prime(list):
    if list == 1:
        return False
    for i in range(2, list):
        if list % i == 0:
            return False
    return True

list1 = list(map(int, input().split()))
list2 = list(filter(lambda x: prime(x), list1))
for i in list2:
    print(i, end = ' ')        

