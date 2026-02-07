from datetime import datetime, date, timedelta

# Додаємо параметр today для тестування
def get_upcoming_birthdays(users, today=None):
    if today is None:
        today = date.today()
    
    upcoming_birthdays = []

    for user in users:
        # Зчитуємо дату народження (враховуємо формат ДД.ММ.РРРР з вашого списку)
        birthday = datetime.strptime(user["дата народження"], "%d.%m.%Y").date()
        
        # Встановлюємо дату народження на поточний рік (2024)
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо ДН вже минув, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи входить в інтервал 7 днів
        days_between = (birthday_this_year - today).days

        if 0 <= days_between <= 7:
            congratulation_date = birthday_this_year

            # Логіка вихідних (5 - субота, 6 - неділя)
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Формуємо словник (ключі як у прикладі результату ТЗ)
            upcoming_birthdays.append({
                "name": user["ім'я"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Дані з вашого прикладу
користувачі = [
    { "ім'я" : "Джон Доу" , "дата народження" : "23.01.1985" },
    { "ім'я" : "Джейн Сміт" , "дата народження" : "27.01.1990" }
]

# Встановлюємо дату "сьогодні" на 22 січня 2024 року
тестова_дата = date(2024, 1, 22)

# Викликаємо функцію з цією датою
upcoming_birthdays = get_upcoming_birthdays(користувачі, today=тестова_дата)

print("Список привітань на цьому тижні:", upcoming_birthdays)