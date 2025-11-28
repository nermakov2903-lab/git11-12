"""
Модуль, содержащий меню задания №2 (вариант 8).

Меню позволяет пользователю:
    — вводить массивы вручную,
    — генерировать массивы автоматически,
    — выполнять анализ (поиск общих чисел),
    — выводить результат.
"""
from logger import logger
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
        logger.info(f"Пользователь выбрал пункт меню: {choice}")
        try:
            if choice == "1":
                try:
                    logger.info("Пользователь вводит массивы вручную")
                    print("Введите первый массив:")
                    arr1 = manual_input_array()
                    print("Введите второй массив:")
                    arr2 = manual_input_array()
                    result = None  # сброс
                    print("Массивы успешно введены.")
                    logger.info(f"Введены массивы:\n arr1={arr1}\n arr2={arr2}")
                except ValueError:
                    raise ValueError("В массив можно вводить только числа или целочисленные")
    
            elif choice == "2":
                logger.info("Пользователь выбрал генерацию массивов")
                n = int(input("Введите размер массивов: "))
                arr1 = generate_array(n)
                arr2 = generate_array(n)
                result = None
                print("Сгенерированы массивы:")
                print("Массив 1:", arr1)
                print("Массив 2:", arr2)
                logger.info(f"Сгенерированы массивы:\n arr1={arr1}\n arr2={arr2}")
    
            elif choice == "3":
                logger.info("Пользователь пытается выполнить анализ")
                try:
                    if arr1 is None or arr2 is None:
                        logger.info("Анализ невозможен: массивы не заданы")
                    raise RuntimeError("Массивы ещё не заданы. Введите их сначала.")

                    result = count_common_numbers(arr1, arr2)
                    logger.info("Анализ успешно выполнен")
                    print("Анализ выполнен.")

                except RuntimeError as e:
                    print("Ошибка:", e)
                    logger.info(f"RuntimeError: {e}")

                except Exception as e:
                    print("Неизвестная ошибка при выполнении анализа:", e)
                    logger.info(f"Неизвестная ошибка: {e}")
    
            elif choice == "4":
                logger.info("Пользователь запросил вывод результата")
                if result is None:
                    raise RuntimeError("Сначала выполните анализ")
                print("Результат:", result)

    
            elif choice == "0":
                logger.info("Возврат в главное меню")
                return

            else:
                logger.info("Пользователь сделал неверный выбор")
                print("Неверный выбор, попробуйте снова.")

    
        except ValueError as e:
            print("Ошибка:", e)
            logger.info(f"ValueError: {e}")
        
        except RuntimeError as e:
            print("Ошибка:", e)
            logger.info(f"RuntimeError: {e}")
        
        except Exception as e:
            print("Неизвестная ошибка:", e)
            logger.info(f"Неизвестная ошибка: {e}")
