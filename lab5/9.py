import re

text = input()
pattern = r'[A-Z]+[a-z]*'
l = re.findall(pattern, text)
print(" ".join(l))
