def read_numbers(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.readlines()

        for line in data:
            line = line.strip()
            if line.isdigit():
                print(line)
            
            else:
                raise TypeError(f"В строке '{line}' найдено значение, отличное от числа.")
            
    except FileNotFoundError:
        print(f"Фвйл '{filename}' не найден.")

    except TypeError as e:
        print(f"Ошибка: {e}")

read_numbers() #Путь или название файла