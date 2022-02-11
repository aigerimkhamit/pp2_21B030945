a, b = input().split("+")
m = [] #for the first number
n = [] #for the second number
for i in range(len(a) // 3):
    m.append(a[i * 3:3 * i + 3])
for i in range(len(b) // 3):
    n.append(b[i * 3: 3 * i + 3])

def func(arr):
    for i in range(len(arr)):
        if arr[i] == "ONE":
            arr[i] = 1
        if arr[i] == "TWO":
            arr[i] = 2
        if arr[i] == "THR":
            arr[i] = 3
        if arr[i] == "FOU":
            arr[i] = 4
        if arr[i] == "FIV":
            arr[i] = 5
        if arr[i] == "SIX":
            arr[i] = 6
        if arr[i] == "SEV":
            arr[i] = 7
        if arr[i] == "EIG":
            arr[i] = 8
        if arr[i] == "NIN":
            arr[i] = 9
        if arr[i] == "ZER":
            arr[i] = 0
func(m)
func(n)
sum = [] # для суммы 
def forsum(mas1, mas2, sum2):
    s = 0
    s1 = 0
    for i in range(len(mas1)):
        s += int(mas1[i] * pow(10, len(mas1) - 1 - i))
    for j in range(len(mas2)):
        s1 += int(mas2[j] * pow(10, len(mas2) - 1 - j))
    sum2.append(s + s1)
forsum(m, n, sum)
str = [str(x) for x in sum] # превращаем в стринг

ans = []

def forout(sumi, answer):
    for i in range(len(sumi[0])):
        if sumi[0][i] == '1':
            answer.append('ONE')
        if sumi[0][i] == '2':
            answer.append('TWO')
        if sumi[0][i] == '3':
            answer.append('THR')
        if sumi[0][i] == '4':
            answer.append('FOU')
        if sumi[0][i] == '5':
            answer.append('FIV')
        if sumi[0][i] == '6':
            answer.append('SIX')
        if sumi[0][i] == '7':
            answer.append('SEV')
        if sumi[0][i] == '8':
            answer.append('EIG')
        if sumi[0][i] == '9':
            answer.append('NIN')
        if sumi[0][i] == '0':
            answer.append('ZER')
forout(str, ans)

for i in range(len(ans)):
    print(ans[i], end = '')
            


