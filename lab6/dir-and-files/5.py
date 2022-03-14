f = open('input.txt', 'a')
f.write('\n')
# f.write(str([1, 2, 4, 5, 'Aigerim', 'happy', 18]))
f.write(str(list(map(int, input().split()))))
f.close()

f = open('input.txt', 'r')
f.read()