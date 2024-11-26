import itertools

def infinite_number_generator(start=0, step=1):
    """Создание бесконечного генератора чисел начиная с `start` и с шагом `step`."""
    return itertools.count(start=start, step=step)

def apply_function_to_iterator(iterator, func):
    """Применение функции `func` к каждому элементу в итераторе `iterator`."""
    return map(func, iterator)

def chain_iterators(*iterators):
    """Объединение нескольких итераторов в один."""
    return itertools.chain(*iterators)

def main():
    try:
        # Задача 1: Создание бесконечного генератора чисел
        infinite_gen = infinite_number_generator(0, 2)
        
        # Вывод первых 10 чисел из бесконечного генератора
        print("Первые 10 чисел из бесконечного генератора:")
        for _ in range(10):
            print(next(infinite_gen), end=" ")
        print()
        
        # Задача 2: Применение функций к каждому элементу в итераторе
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = apply_function_to_iterator(numbers, lambda x: x ** 2)
        
        print("Квадраты чисел из списка [1, 2, 3, 4, 5]:")
        for num in squared_numbers:
            print(num, end=" ")
        print()
        
        # Задача 3: Объединение нескольких итераторов в один
        iterator1 = [1, 2, 3]
        iterator2 = ['a', 'b', 'c']
        combined_iterator = chain_iterators(iterator1, iterator2)
        
        print("Объединенные итераторы [1, 2, 3] и ['a', 'b', 'c']:")
        for item in combined_iterator:
            print(item, end=" ")
        print()
    
    except StopIteration:
        print("Итератор завершил работу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
