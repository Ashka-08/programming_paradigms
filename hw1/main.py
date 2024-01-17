from random import randint


def create_list(size: int) -> list:
    lst = []
    for i in range(size):
        lst.append(randint(1, 99))
    return lst


def sort_list_imperative(numbers: list) -> list:
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def sort_list_declarative(numbers: list) -> list:
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    print('Created list: \n', lst := create_list(10))
    print(f'Imperative:\n {sort_list_imperative(lst)}')
    print(f'Declarative:\n {sort_list_declarative(lst)}')
