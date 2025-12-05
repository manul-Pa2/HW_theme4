import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:      #Повертаємо відсортований список з унікальних випадкових чисел
    
    if min < 1 or max > 1000 or min >= max:        # Перевіряємо межі діапазону
        return []

    if quantity < 1 or quantity > (max - min + 1):    # Перевіряємо коректність quantity
        return []

    numbers = random.sample(range(min, max + 1), quantity)    # одразу повертаємо унікальні числа без повторів

    numbers.sort()   # Сортуємо
    return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші лотерейні номери:", lottery_numbers)      # Перевірка як у прикладі
