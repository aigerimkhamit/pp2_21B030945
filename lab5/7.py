import re

def stc(text):
    retext = re.split('_', text)
    for i in range(len(retext)):
        retext[i] = retext[i].capitalize()
    return ''.join(retext)

text = "dana_loves_eating_bananas"
print(stc(text))