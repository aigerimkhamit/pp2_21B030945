word = input()
letter = input()
x = word.find(letter) # we use it to find the first position 
y = word.rfind(letter) # the second
if x == y:
    print(x)
else:
    print(x, y)


