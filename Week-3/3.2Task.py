print("--- Задание 2: Сортировка букв в словах ---")

text = input("Введите предложение на английском: ")

words = text.split() 

sorted_words = []

for word in words:
    letters_list = sorted(word)
    
    new_word = "".join(letters_list)
    
    sorted_words.append(new_word)

result_text = " ".join(sorted_words)

print(f"Результат: {result_text}")