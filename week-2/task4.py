line = input().split()
n = int(line[0])
m = int(line[1])

s = input().strip()

words = set()

for i in range(n - m + 1):
    sub = s[i : i + m]
    words.add(sub)

print(len(words))