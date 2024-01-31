# Будем использовать функциональную, процедурную и структурную парадигму.
# С одной стороны, используем функции create_random_array, get_random_number и 
# binary_search, что определяет процедурную парадигму.
#  С другой стороны, используем функции randint, choice, len и max,
# которые в нашем случае являются черными ящиками, что характерно для
# функциональной парадигмы.
# Также, программа имеет четкую последовательсть шагов, а значит 
# остается в рамках структурной парадигмы

from random import randint, choice


def create_random_array(count: int, max_number: int) -> list:
    """Функция создания массива с помощью библиотки random
    :param count: требуемая длина массива.
    :param max_number:  макисмальное значение в массиве.
    :return: Сортированный массив"""
    i = 0
    arr = []
    while i < count:
        item = randint(0,max_number)
        if item not in arr:
            arr.append(item)
            i+=1
    res = sorted(arr)
    return res


def get_random_number(arr: list) -> int:
    """Функция получения элемента с помощью библиотки random
    :param arr: массив целых чисел
    :return: рандомный элемент массива"""
    first = randint(0, max(arr))
    second = choice(arr)
    return choice((first, second))


def binary_search(arr: list, number: int) -> int:
    """Функция бинарного поиска элемента в массиве
    :param arr: массив целых чисел.
    :param number: целое число для поиска
    :return: индекс элемент массива или значение '-1', 
    если элемент отстутствует в массиве"""
    left = 0
    right = len(arr) - 1
    while left <= right:
        center = (left + right) // 2
        if arr[center] == number:
            return center
        elif arr[center] < number:
            left = center + 1
        else:
            right = center - 1
    return -1


if __name__ == "__main__":
    for _ in range(5):
        arr = create_random_array(10,100)
        print(f'Массив: {arr}')
        number = get_random_number(arr)
        print(f"Число для поиска: {number}")
        print(f"Результат бинарного поиска: {binary_search(arr, number)}\n")