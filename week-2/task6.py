def all_eq(lst):
    if not lst:
        return []
    m = max(len(s) for s in lst)
    return [s + "_" * (m - len(s)) for s in lst]

line = input()
words = line.split()

print(all_eq(words))