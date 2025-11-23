from menu_task8 import menu_task8

def main():
    while True:
        print("Главное меню ")
        print("1. Задание №2")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            menu_task8()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Ошибка: нет такого пункта меню!")

if __name__ == "__main__":
    main()
