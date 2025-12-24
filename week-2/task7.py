items = input().split()

counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("Purchase frequency:")
for item in counts:
    print(f"{item}: {counts[item]}")

most_popular = ""
max_count = 0
for item in counts:
    if counts[item] > max_count:
        max_count = counts[item]
        most_popular = item

print("Most popular item:", most_popular)

once_items = []
for item in counts:
    if counts[item] == 1:
        once_items.append(item)

print("Purchased once:", " ".join(once_items))

print("Sorted by frequency:")
sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for item, count in sorted_list:
    print(item, count)