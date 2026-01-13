import json

def process_grades():
    input_file = 'students.json'
    output_file = 'students_analyzed.json'

    # 1. Читаем данные из файла
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f) # json.load превращает текст из файла в список Python
    except FileNotFoundError:
        print(f"ОШИБКА: Файл {input_file} не найден!")
        return

    # 2. Проходимся по каждому студенту и считаем средний балл
    for student in data:
        grades = student['grades']
        # Сумма оценок делить на количество оценок
        average = sum(grades) / len(grades)
        # Округляем до 2 знаков после запятой (чтобы было красиво)
        student['average_grade'] = round(average, 2)

    # 3. Записываем обновленные данные в НОВЫЙ файл
    with open(output_file, 'w', encoding='utf-8') as f:
        # json.dump превращает список Python обратно в текст
        # indent=4 делает красивый отступ, чтобы было удобно читать
        json.dump(data, f, indent=4)
    
    print(f"Готово! Данные обработаны и сохранены в {output_file}")

if __name__ == "__main__":
    process_grades()