from src.array_merge import merge_arrays

def main():
    print("Тест объединения массивов:")
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print("arr1:", arr1)
    print("arr2:", arr2)
    print("Объединение:", merge_arrays(arr1, arr2))

if __name__ == "__main__":
    main()