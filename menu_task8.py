from array_input import manual_input_array
from array_generate import generate_array
from task8_common_numbers import count_common_numbers

def menu_task8():
    arr1 = None
    arr2 = None
    result = None

    while True:
        print("Меню задания 8")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Выполнить алгоритм")
        print("4. Вывести результат")
        print("0. Назад")

        choice = input("Выберите пункт: ")

        if choice == "1":
            print("\nВвод первого массива:")
            arr1 = manual_input_array()

            print("Ввод второго массива:")
            arr2 = manual_input_array()

            result = None
            print("Данные введены.")

        elif choice == "2":
            n = int(input("Размер массивов: "))
            arr1 = generate_array(n)
            arr2 = generate_array(n)

            result = None
            print("Массивы сгенерированы.")
            print("arr1 =", arr1)
            print("arr2 =", arr2)

        elif choice == "3":
            if arr1 is None or arr2 is None:
                print("Ошибка: массивы не введены!")
            else:
                result = count_common_numbers(arr1, arr2)
                print("Алгоритм выполнен.")

        elif choice == "4":
            if result is None:
                print("Ошибка: алгоритм не выполнен!")
            else:
                print("Количество общих чисел:", result)

        elif choice == "0":
            break

        else:
            print("Нет такого пункта меню!")