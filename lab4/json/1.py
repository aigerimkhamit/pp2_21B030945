import json
f = open('sample-data.json', 'r')
text = f.read()
new = json.loads(text)
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')
s1 = '                              '
s2 = '   '
x = new['imdata']
for i in range(len(x)):
    a = x[i]["l1PhysIf"]['attributes']['dn'] 
    b = x[i]["l1PhysIf"]['attributes']['speed']
    c = x[i]["l1PhysIf"]['attributes']['mtu']
    print(a, s1, b, s2, c)
