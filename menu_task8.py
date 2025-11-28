"""
Модуль, содержащий меню задания №2 (вариант 8).

Меню позволяет пользователю:
    — вводить массивы вручную,
    — генерировать массивы автоматически,
    — выполнять анализ (поиск общих чисел),
    — выводить результат.
"""

from array_input import manual_input_array
from array_generate import generate_array
from task8_common_numbers import count_common_numbers

def menu_task8():
    """
    Запускает диалоговое меню выполнения задания №2.

    Пользователь может:
        1. Ввести массивы вручную.
        2. Сгенерировать массивы случайным образом.
        3. Запустить алгоритм вычисления.
        4. Просмотреть результат.
        0. Вернуться в главное меню.

    При вводе новых данных результаты анализа автоматически сбрасываются.
    """

    arr1 = None      # Первый массив
    arr2 = None      # Второй массив
    result = None    # Результат анализа

    while True:
        print("\n--- Меню задания №2 ---")
        print("1. Ввести два массива вручную")
        print("2. Сгенерировать два массива")
        print("3. Выполнить анализ (общие + перевёрнутые числа)")
        print("4. Вывести результат")
        print("0. Назад в главное меню")

        choice = input("Ваш выбор: ")

        if choice == "1":
            print("Введите первый массив:")
            arr1 = manual_input_array()
            print("Введите второй массив:")
            arr2 = manual_input_array()
            result = None  # сброс
            print("Массивы успешно введены.")

        elif choice == "2":
            n = int(input("Введите размер массивов: "))
            arr1 = generate_array(n)
            arr2 = generate_array(n)
            result = None
            print("Сгенерированы массивы:")
            print("Массив 1:", arr1)
            print("Массив 2:", arr2)

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: массивы ещё не заданы.")
            else:
                result = count_common_numbers(arr1, arr2)
                print("Анализ выполнен.")

        elif choice == "4":
            if result is None:
                print("Ошибка: нет результата. Сначала выполните анализ.")
            else:
                print("Количество общих чисел (с учетом перевёрнутых):", result)

        elif choice == "0":
            return

        else:
            print("Неверный выбор, попробуйте снова.")
