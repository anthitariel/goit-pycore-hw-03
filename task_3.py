import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Якщо номер починається з '+', перевіряємо чи це повний код
    if cleaned_number.startswith('+'):
        if not cleaned_number.startswith('+38'):
            # Тут можна додати логіку для інших країн, але за умовою фокусуємось на +38
            pass
    elif cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    else:
        # Якщо номер без коду країни (наприклад, 050...)
        cleaned_number = '+38' + cleaned_number
        
    return cleaned_number

# Приклад використання
raw_numbers = [
     "067\\t123 4567" ,
     "(095) 234-5678\\n" ,
     "+380 44 123 4567" ,
     "380501234567" ,
     "+38(050)123-32-34" ,
     "0503451234" ,
     "(050)8889900" ,
     "38050-111-22-22" ,
     "38050 111 22 11" ,
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)