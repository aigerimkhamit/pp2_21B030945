s = input()
a = []

for i in s:
    if  i == "{" or i == "[" or i == "(":
        a.append(i)
    else:
        if len(a) == 0:
           print("No")
           exit()
        if (i == "}" and a[-1] == "{") or (i == "]" and a[-1] == "[") or (i == ")" and a[-1] == "("):
            a.pop(-1)
if len(a) == 0:
    print("Yes")
else:
    print("No")
