from task8_common_numbers import count_common_numbers
from menu_task8 import menu_task8

def main():
    print("Тест алгоритма задания 8:")
    arr1 = [12, 23, 34, 45]
    arr2 = [21, 23, 43, 50]
    print("arr1:", arr1)
    print("arr2:", arr2)
    result = count_common_numbers(arr1, arr2)
    print("Количество общих чисел (с учётом переворота):", result)

    
    print("Запуск меню задания 8")
    menu_task8()

if __name__ == "__main__":
    main()
