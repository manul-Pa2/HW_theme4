from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:         # Кожен елемент результату має вигляд:"name": <ім'я користувача>, "congratulation_date": "YYYY.MM.DD"

    today = date.today()      # Якщо день народження припадає на суботу або неділю, дата привітання переноситься на наступний понеділок.
    result = []

    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()     # Дата народження як date-об'єкт

        birthday_this_year = birthday.replace(year=today.year)       # День народження у поточному році

        if birthday_this_year < today:                                                    # Якщо в цьому році день народження вже минув — беремо наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days          # Різниця в днях між сьогодні та днем народження

        if 0 <= delta_days <= 7:                       # Цікавлять тільки ті, що в межах 0–7 днів включно
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:            # Якщо це субота (5) або неділя (6) — переносимо на понеділок
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result

""" 
#TEST users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
"""
