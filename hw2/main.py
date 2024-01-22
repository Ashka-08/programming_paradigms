def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} * {j} = {i * j}')
        print()

if __name__ == "__main__":
    print("Процедурная парадигма для переиспользования кода в программе")
    multiplication_table(1)
    print()
    multiplication_table(3)

    print("Структурная парадигма без переиспользования кода в программе")
    n = int(input("Введите число: "))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} * {j} = {i * j}')
        print()