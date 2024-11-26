from datetime import datetime, timedelta

def display_current_datetime():
    """Отображает текущую дату и время."""
    current_datetime = datetime.now()
    print(f"Текущая дата и время: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_date_difference(date1_str, date2_str):
    """
    Вычисляет разницу между двумя датами.
    :param date1_str: Первая дата в формате 'YYYY-MM-DD'.
    :param date2_str: Вторая дата в формате 'YYYY-MM-DD'.
    """
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    difference = abs(date2 - date1)
    print(f"Разница между {date1_str} и {date2_str}: {difference.days} дней")

def convert_string_to_datetime(date_str, format='%Y-%m-%d'):
    """
    Преобразует строку в объект даты и времени.
    :param date_str: Строка с датой.
    :param format: Формат строки (по умолчанию 'YYYY-MM-DD').
    """
    try:
        date_obj = datetime.strptime(date_str, format)
        print(f"Преобразованная дата: {date_obj}")
    except ValueError:
        print(f"Ошибка: строка '{date_str}' не соответствует формату '{format}'.")

# Пример использования
if __name__ == "__main__":
    # 1. Отображение текущей даты и времени
    display_current_datetime()

    # 2. Вычисление разницы между двумя датами
    calculate_date_difference('2024-01-01', '2024-11-26')

    # 3. Преобразование строки в объект даты и времени
    convert_string_to_datetime('2024-11-26', '%Y-%m-%d')
