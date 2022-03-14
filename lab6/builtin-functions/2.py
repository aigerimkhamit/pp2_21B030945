s = input()

def cnt(s):
    sumu = 0
    suml = 0
    for i in s:
        if i.isupper():
            sumu += 1
        if i.islower():
            suml += 1
    return sumu, suml

print(cnt(s))
