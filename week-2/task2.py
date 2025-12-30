a = input()
b = input()

valid_shifts = []
n = len(b)

for i in range(n):
    shift = b[i:] + b[:i]
    valid_shifts.append(shift)

count = 0

for i in range(len(a) - n + 1):
    sub_string = a[i : i + n]
    
    if sub_string in valid_shifts:
        count += 1

print(count)