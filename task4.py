# Task 4: Employee Hierarchy

# 1. Базовый класс
class Employee:
    def __init__(self, name, salary):
        self.name = name
        # ПРИВАТНЫЙ атрибут (скрыт от прямого доступа)
        self._salary = salary 

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

# 2. Дочерний класс (Наследование)
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Переопределение метода (Override)
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

# 3. ФУНКЦИЯ по условию задачи:
# Принимает список объектов Employee и Manager
def display_employees(employees_list):
    print(f"{'Role':<10} | {'Name':<10} | {'Salary':<10}")
    print("-" * 35)
    for emp in employees_list:
        # Здесь работает ПОЛИМОРФИЗМ: вызывается нужный get_role()
        role = emp.get_role()
        salary = emp.get_salary()
        print(f"{role:<10} | {emp.name:<10} | {salary:<10}")

# Демонстрация
if __name__ == "__main__":
    # Создаем список из разных объектов
    staff = [
        Employee("Alice", 50000),
        Manager("Bob", 80000, 15000),
        Employee("Charlie", 45000)
    ]
    
    display_employees(staff)    