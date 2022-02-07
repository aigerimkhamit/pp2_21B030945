n = int(input())
you = dict()

for i in range(n):
    name, payment = map(str, input().split())
    if name in you:
        you[name] += int(payment)
    else:
        you[name] = int(payment)

maxi = max(you.values())

for key, value in sorted(you.items()):
    if value == maxi:
        print(f"{key} is lucky!")
    else:
        print(f"{key} has to receive {maxi - int(value)} tenge")