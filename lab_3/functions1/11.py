def rev(s):
    k = s[::-1]
    if k == s:
        return True
    return False
s = input()
print(rev(s))