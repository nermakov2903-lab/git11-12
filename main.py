from src.array_sort import sort_array
from src.array_input import manual_input_array

def main():
    print("Тест функции ручного ввода массива:")
    arr = manual_input_array()
    print("Вы ввели:", arr)


    print("Тест сортировки массива:")
    arr = [5, 1, 4, 2, 3]
    print("Исходный:", arr)
    print("Отсортированный:", sort_array(arr))

if __name__ == "__main__":
    main()
