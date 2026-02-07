import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка коректності вхідних даних
    if not (1 <= min_val <= quantity <= max_val <= 1000):
        return []
    
    # Створюємо список усіх чисел у діапазоні та вибираємо випадкові унікальні
    numbers = range(min_val, max_val + 1)
    ticket = random.sample(numbers, k=quantity)
    
    # Повертаємо відсортований список
    return sorted(ticket)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)