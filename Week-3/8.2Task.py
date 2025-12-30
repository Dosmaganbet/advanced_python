print("--- Часть 2: Замена первого и последнего элемента ---")

def swap_first_last(array_list):

    if len(array_list) < 2:
        return

    array_list[0], array_list[-1] = array_list[-1], array_list[0]

m = int(input("Введите длину массива (m): "))
my_array = []

print(f"Введите {m} элементов по одному:")
for i in range(m):
    val = int(input(f"  Элемент {i+1}: "))
    my_array.append(val)

print(f"Оригинальный массив: {my_array}")

swap_first_last(my_array)

print(f"Измененный массив:   {my_array}")