import re

def searchcorrect(text):
    pattern = r'^a(b*)$'
    if re.search(pattern, text):
        print("Well done")
    else:
        print("That's a pity")
text = input()
searchcorrect(text)
