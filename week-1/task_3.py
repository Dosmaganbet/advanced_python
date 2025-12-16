a = input()

parts = a.split(".")

integer_part = parts[0]
fractional_part = parts[1]

print(fractional_part + "." + integer_part)
