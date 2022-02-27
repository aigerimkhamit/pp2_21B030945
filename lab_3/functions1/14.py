# Adil' was given a neccessary quantity of apples and he was also given a list numbers in which 
# he musts to put the apples in the form of histogram. But before he starts, he needs to check given list 
# for prime numbers. Help him to do this.

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
def histogram(list):
    for i in list:
        for x in range(i):
            print("*", end = '')
        print()
histogram(list2)  