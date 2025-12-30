salaries = input().split()

a = int(salaries[0])
b = int(salaries[1])
c = int(salaries[2])

maximum = max(a, b, c)
minimum = min(a, b, c)

difference = maximum - minimum

print(difference)