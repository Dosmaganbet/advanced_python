# Task 3: OOP Principles

# 1. Base Class (Родительский класс)
class Person:
    def __init__(self, name, age):
        self.name = name
        # ИНКАПСУЛЯЦИЯ: _age с одним подчеркиванием. 
        # Это значит "не трогай меня напрямую, я для внутреннего пользования".
        self._age = age 

    def introduce(self):
        return f"Hi, I am {self.name} and I am {self._age} years old."

# 2. Child Class (Дочерний класс - НАСЛЕДОВАНИЕ)
# Student наследует всё от Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Вызываем конструктор родителя (Person)
        super().__init__(name, age) 
        self.student_id = student_id

    # ПОЛИМОРФИЗМ (Override):
    # Мы переписываем метод introduce. У студента он работает иначе, чем у человека.
    def introduce(self):
        # Используем базовое представление + добавляем ID
        base_intro = super().introduce()
        return f"{base_intro} My Student ID is {self.student_id}."

# 3. Demonstration (Проверка)
if __name__ == "__main__":
    # Создаем обычного человека
    person = Person("John", 40)
    
    # Создаем студента
    student = Student("Mike", 20, "S12345")

    print("--- Polymorphism Demo ---")
    # Один и тот же метод .introduce() выдает разный результат
    print(person.introduce())  
    print(student.introduce())

    print("\n--- Encapsulation Demo ---")
    # Мы можем получить доступ к _age, но Python намекает подчеркиванием, что так делать не надо.
    # На защите скажи: "_age is protected attribute".
    print(f"Accessing protected attribute: {person._age}")