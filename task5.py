# Task 5: BankAccount with Validation

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Двойное подчеркивание — СТРОГО ПРИВАТНЫЕ атрибуты
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        # Валидация: депозит должен быть положительным
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Error: Deposit amount must be positive!")

    def withdraw(self, amount):
        # Валидация: нельзя снять больше, чем есть, и нельзя снять минус
        if amount > self.__balance:
            print("Error: Insufficient funds!")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Проверка
if __name__ == "__main__":
    acc = BankAccount("Dmitry", 1000)
    
    acc.deposit(500)   # Ок
    acc.withdraw(200)  # Ок
    acc.withdraw(2000) # Ошибка (недостаточно средств)
    acc.deposit(-50)   # Ошибка (отрицательный депозит)
    
    print(f"Final balance for {acc._BankAccount__owner}: {acc.get_balance()}")