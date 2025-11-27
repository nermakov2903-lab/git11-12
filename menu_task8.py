"""
Модуль, содержащий меню задания №2 (вариант 8).

Меню позволяет пользователю:
    — вводить массивы вручную,
    — генерировать массивы автоматически,
    — выполнять анализ (поиск общих чисел),
    — выводить результат.
"""
from logger import logger
from messages import Messages
from exceptions import *
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
        print(Messages.MENU_TASK8["title"])
        print(Messages.MENU_TASK8["manual"])
        print(Messages.MENU_TASK8["generate"])
        print(Messages.MENU_TASK8["analyze"])
        print(Messages.MENU_TASK8["result"])
        print(Messages.MENU_TASK8["back"])
        
        choice = input(Messages.MENU_TASK8["prompt"])
        logger.info(f"Пользователь выбрал пункт меню: {choice}")
        try:
            if choice == "1":
                logger.info("Пользователь вводит массивы вручную")
                try:
                    print(Messages.MENU_TASK8.get("input_arr1", "Введите первый массив:"))
                    arr1 = manual_input_array()
                    print(Messages.MENU_TASK8.get("input_arr2", "Введите второй массив:"))
                    arr2 = manual_input_array()
                    result = None  # сброс
                    print(Messages.ACTIONS.get("arrays_entered", "Массивы успешно введены."))
                    logger.info(f"Введены массивы:\n arr1={arr1}\n arr2={arr2}")
                except ValueError as e:
                    logger.error("В массив введены нечисловые значения")
                    raise InvalidNumberError(Messages.ERRORS.get("not_number", "Ошибка: вводите только числа!"))
    
            elif choice == "2":
                logger.info("Генерация массивов")
                try:
                    n = int(input(Messages.MENU_TASK8.get("size_prompt", "Введите размер массивов: ")))
                    arr1 = generate_array(n)
                    arr2 = generate_array(n)
                    result = None
                    print(Messages.ACTIONS.get("arrays_generated", "Сгенерированы массивы:"))
                    print("Массив 1:", arr1)
                    print("Массив 2:", arr2)
                    logger.info(f"Сгенерированы массивы:\n arr1={arr1}\n arr2={arr2}")
                except ValueError as e:
                    logger.info(f"Ошибка при генерации массивов: {e}")
                    raise InvalidNumberError(Messages.ERRORS.get("not_number", "Ошибка: вводите только числа!"))
    
             elif choice == "3":
                logger.info("Выполнение анализа")
                if arr1 is None or arr2 is None:
                    logger.info("Анализ невозможен: массивы не заданы")
                    raise EmptyArrayError(Messages.ERRORS.get("no_result", "Массивы ещё не заданы. Введите их сначала."))
                result = count_common_numbers(arr1, arr2)
                print(Messages.ACTIONS.get("analysis_done", "Анализ выполнен."))
                logger.info(f"Анализ завершён. Результат: {result}")
    
            elif choice == "4":
                logger.info("Запрос вывода результата")
                if result is None:
                    raise EmptyArrayError(Messages.ERRORS.get("no_result", "Сначала выполните анализ"))
                print(Messages.ACTIONS.get("result_label", "Результат:"), result)
                logger.info(f"Результат выведен: {result}")

    
            elif choice == "0":
                logger.info("Возврат в главное меню")
                return

             else:
                logger.info(f"Неверный выбор меню: {choice}")
                raise InvalidMenuChoiceError(Messages.ERRORS.get("invalid_choice", "Неверный выбор, попробуйте снова."))


    
     except InvalidNumberError as e:
            print("Ошибка:", e)
            logger.info(f"InvalidNumberError: {e}")

        except EmptyArrayError as e:
            print("Ошибка:", e)
            logger.info(f"EmptyArrayError: {e}")

        except InvalidMenuChoiceError as e:
            print("Ошибка:", e)
            logger.info(f"InvalidMenuChoiceError: {e}")

        except Exception as e:
            print(Messages.ERRORS.get("unknown", "Произошла неизвестная ошибка!"))
            logger.info(f"Неизвестная ошибка: {e}")
