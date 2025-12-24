s = input().strip().replace(" ", "")

a = s[0]
op = s[1]
b = s[2]
c = s[4]

if op == '+':
    if a == 'x':
        x = int(c) - int(b)
    elif b == 'x':
        x = int(c) - int(a)
    else:
        x = int(a) + int(b)
else:
    if a == 'x':
        x = int(c) + int(b)
    elif b == 'x':
        x = int(a) - int(c)
    else:
        x = int(a) - int(b)

print(x)