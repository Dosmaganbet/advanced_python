array1 = [10, 20, 30, 40, 50]
array2 = [5, 15, 25, 35, 45, 55, 65]
array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

all_arrays = [array1, array2, array3]

count = 1

for current_array in all_arrays:
    total_sum = sum(current_array)
    
    length = len(current_array)
    
    if length > 0:
        mean = total_sum / length
    else:
        mean = 0

    print(f"--- Массив {count} ---")
    print(f"Элементы: {current_array}")
    print(f"Сумма: {total_sum}")
    print(f"Среднее арифметическое: {mean}")
    print("")
    
    count += 1