a = list(map(int, input().split()))

def multiple(a):
    ans = 1
    for i in a:
        ans = ans * i
    return ans
print(multiple(a))