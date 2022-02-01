mess = input()

def findleng(s):
    cnt = 0
    for i in s:
        cnt += 1
    return cnt

word = ""
ans = ""

for i in range(len(mess)):
    if mess[i] != " ":
        word += mess[i]
    if mess[i] == " ":
        if findleng(word) >= 3:
            ans = ans + word + " "
        word = "" # обновляем значение
    if i == len(mess) - 1: # тут проверяем, чтобы после последнего слова не выводило пробел
        if findleng(word) >= 3:
            ans += word

print(ans) 