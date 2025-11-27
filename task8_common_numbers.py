from logger import logger
"""
Модуль реализации алгоритма задания №2 (вариант 8):
Определение количества чисел, которые совпадают или имеют совпадающую
'перевёрнутую' версию в другом массиве.
"""

def reverse_number(n: int) -> int:
    logger.info(f"Вызов reverse_number() с аргументом: {n}")
    """
    Возвращает перевёрнутую версию целого числа.

    Примеры:
        123 → 321  

    Args:
        n (int): Число, которое требуется развернуть.

    Returns:
        int: Перевёрнутое число с тем же знаком.
    """
    if not isinstance(n, int):
        logger.info("reverse_number получил не число")
        raise ValueError("Ожидалось целое число")
        
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_str = str(n)[::-1]
    result = sign * int(reversed_str)

    logger.info(f"Результат reverse_number(): {result}")
    return result


def count_common_numbers(arr1, arr2):
    logger.info(f"Вызов count_common_numbers() с массивами:\n  arr1={arr1}\n  arr2={arr2}")
    """
    Подсчитывает количество чисел, общих для двух массивов,
    включая случаи, когда совпадает перевёрнутая версия числа.

    Логика работы:
        1. Преобразуем второй массив в множество для быстрого поиска.
        2. Для каждого элемента arr1 проверяем:
            - содержится ли он в arr2,
            - либо содержится ли в arr2 его перевёрнутая версия.
        3. Подсчитываем количество совпадений.

    Args:
        arr1 (list[int]): Первый массив чисел.
        arr2 (list[int]): Второй массив чисел.

    Returns:
        int: Количество найденных совпадений.
    """
    if arr1 is None or arr2 is None:
        logger.info("Один из массивов не был задан")
        raise RuntimeError("Массивы должны быть заданы")
        
    set2 = set(arr2)
    count = 0

    for num in arr1:
        try:
            reversed_num = reverse_number(num)
        except ValueError as e:
            # Ошибка внутри reverse_number — продолжаем
            logger.info(f"Ошибка reverse_number: {e}")
            continue
            
        if num in set2 or reversed_num in set2:
            count += 1
            
    logger.info(f"Результат count_common_numbers(): {count}")
    return count
