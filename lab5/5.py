import re

def correct(text):
    pattern = 'a.*?b$'
    if re.search(pattern, text):
        print("Well done")
    else:
        print("That's a pity")

text = input()
correct(text)