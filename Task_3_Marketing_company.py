import re

def normalize_phone(phone_number: str) -> str:    # Створюємо нормалізатор)

    phone = phone_number.strip()     # Чистимо від зайвих пробілів

    has_plus = phone.startswith("+")      # Чи є '+' на початку

    digits = re.sub(r"\D", "", phone)     # Відсортовуємо лише цифри

    if not digits:       #Обробляємо помилку порожнього рядку
        return ""

    if has_plus:               # Якщо номер уже був із '+', вважаємо, що код уже є
        return f"+{digits}"

    if digits.startswith("380"):       # Якщо номер починається з '380' — це повний міжнародний формат без '+'
        return f"+{digits}"

    return f"+38{digits}"     # Інакше це локальний номер, додаємо код країни '+38'
