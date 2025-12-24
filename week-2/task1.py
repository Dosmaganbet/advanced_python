s = input()
count = 0
for i in range(len(s) - 4):

    part = s[i : i+5]

    if part == ">>-->" or part == "<--<<":
        count = count + 1

print(count)