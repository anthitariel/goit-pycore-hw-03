from datetime import datetime, date

def get_days_from_today(date_str: str): # Прибираємо -> int, бо можемо повернути None або рядок
    """
    Повертає кількість днів між заданою датою та поточною датою.
    Формат дати: 'YYYY-MM-DD'
    """
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        delta = today - given_date
        return delta.days
    except (ValueError, TypeError):
        # Повертаємо повідомлення або None, щоб програма не "падала"
        print("Помилка: Неправильний формат дати. Очікується 'YYYY-MM-DD'.")
        return None

# Приклад використання
print(get_days_from_today("2021-10-09"))