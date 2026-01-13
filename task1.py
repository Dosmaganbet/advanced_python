import string

# Эта функция убирает запятые и точки, чтобы "Code" и "code." были одним словом
def clean_word(word):
    # Таблица для удаления знаков препинания
    translator = str.maketrans('', '', string.punctuation)
    return word.translate(translator).lower()

def main():
    # 1. Читаем файл
    try:
        with open("text.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("ОШИБКА: Файл text.txt не найден! Проверь, что он в той же папке.")
        return

    total_lines = len(lines)
    word_counts = {}
    total_words = 0

    # 2. Обрабатываем каждую строку
    for line in lines:
        # Разбиваем строку на слова по пробелам
        words_in_line = line.split()
        for word in words_in_line:
            # Чистим слово от мусора
            clean = clean_word(word)
            if clean: # Если слово не пустое
                total_words += 1
                # Если слово уже было - увеличиваем счетчик, если нет - ставим 1
                if clean in word_counts:
                    word_counts[clean] += 1
                else:
                    word_counts[clean] = 1

    # 3. Записываем результат в файл analysis.txt
    with open("analysis.txt", "w", encoding="utf-8") as outfile:
        outfile.write(f"Total lines: {total_lines}\n")
        outfile.write(f"Total words: {total_words}\n")
        outfile.write("Word frequencies:\n")
        for word, count in word_counts.items():
            outfile.write(f"{word}: {count}\n")
    
    print("Готово! Проверь файл analysis.txt в папке.")

if __name__ == "__main__":
    main()