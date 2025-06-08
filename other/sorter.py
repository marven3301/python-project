# sorter.py

def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_from_input():
    raw = input("Введите числа через пробел: ")
    try:
        numbers = [int(num) for num in raw.strip().split()]
    except ValueError:
        return "Ошибка: нужно вводить только числа через пробел."

    sorted_numbers = bubble_sort(numbers)
    return f"Отсортированный список: {sorted_numbers}"
