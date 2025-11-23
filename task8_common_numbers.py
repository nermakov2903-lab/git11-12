def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    return sign * int(str(n)[::-1])

def count_common_numbers(arr1, arr2):
    set2 = set(arr2)
    result = 0

    for num in arr1:
        rev = reverse_number(num)
        if num in set2 or rev in set2:
            result += 1

    return result