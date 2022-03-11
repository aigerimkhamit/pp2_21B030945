import re

def cts(text):
    a = re.findall('[A-Z]+[a-z]*', text)
    for i in range(len(a)):
        a[i] = a[i].casefold()
    return "_".join(a)
text = "DanaLovesEatinChipsVeryMuch"
print(cts(text))