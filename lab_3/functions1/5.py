import itertools
s = input()
def permut(s):
    k = list(itertools.permutations(s))
    for i in k:
        print(''.join(i), end = " ")
permut(s)
