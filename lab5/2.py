import re

def searchcorrect(text):
    pattern = 'ab{2,3}'
    if re.search(pattern, text):
        print("Well done")
    else:
        print("That's a pity")

text = input()
searchcorrect(text)