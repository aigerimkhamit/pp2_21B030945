import re

def correct(text):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, text):
        print("Well done")
    else:
        print("That's a pity")

text = input()
correct(text)