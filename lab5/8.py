import re

pattern = '[A-Z][^A-Z]*'
text = input()
print(re.findall(pattern, text))