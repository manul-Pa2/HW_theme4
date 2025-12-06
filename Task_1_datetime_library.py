from datetime import datetime

def get_days_from_today(date: str) -> int:      #Повертає кількість днів між заданою датою та поточною датою
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()     #Переводимо рядо у дату

    except ValueError:
        raise ValueError("Дата має бути у форматі 'YYYY-MM-DD', наприклад '2020-10-09'")    #Перевірка на помилку

    
    today = datetime.today().date()      #Сбогоднішня дата, без часу

    delta = today - target_date
    return delta.days
