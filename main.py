"""
Главный модуль программы.
Обеспечивает интерфейс верхнего уровня и доступ к заданиям программы.

Требования:
    — Меню верхнего уровня.
    — Вызов вложенных меню для выполнения отдельных задач.
    — Завершение работы программы.
"""
from logger import logger
from messages import Messages
from menu_task8 import menu_task8
from exceptions import InvalidMenuChoiceError

def main():
    """
    Запускает главное меню программы.

    Пользователь может:
        — перейти к выполнению задания №2,
        — завершить работу приложения.
    """
    print("=== Программа: задание №2 ===")

    while True:
        print(Messages.MENU_MAIN["title"])
        print(Messages.MENU_MAIN["choose_task"])
        print(Messages.MENU_MAIN["disable_log"])
        print(Messages.MENU_MAIN["exit"])

        choice = input(Messages.MENU_MAIN["prompt"])
        logger.info(f"Пользователь выбрал пункт главного меню: {choice}")

        try:
            if choice == "1":
                logger.info("Запуск меню задания №2")
                menu_task8()
                
            elif choice == "2":
                logger.setLevel("CRITICAL")
                logger.critical("Логи ниже уровня CRITICAL теперь отключены")
                print(Messages.ACTIONS["logs_off"])
                
            elif choice == "0":
                logger.info("Завершение работы программы")
                break
            else:
                raise InvalidMenuChoiceError(choice)

        except InvalidMenuChoiceError as e:
            print("Ошибка:", e)
            logger.error(f"Меню: {e}")

        except Exception as e:
            print("Неизвестная ошибка")
            logger.critical(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

