print("--- Часть 1: Числа, которые делятся на свои цифры ---")

n = int(input("Введите число n: "))

print(f"Числа от 1 до {n}, которые делятся на каждую свою цифру:")

for number in range(1, n + 1):
    s_num = str(number)
    
    if '0' in s_num:
        continue
    
    is_good = True
    
    for digit_char in s_num:
        digit = int(digit_char)
        
        if number % digit != 0:
            is_good = False
            break
            
    if is_good:
        print(number, end=" ")

print("\n" + "-" * 30)