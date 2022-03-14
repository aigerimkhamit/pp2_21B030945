def cntlines(file):
    cnt = 0
    with open(file, 'r') as f:
        for line in f:
            cnt = cnt + 1
    return cnt
print(cntlines('input.txt'))