# Задача 2

input_number = int(input("Введите число (от 1 до 100000): "))
MIN_LIMIT = 0
MAX_LIMIT = 100000


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


if MIN_LIMIT < input_number < MAX_LIMIT:
    if is_prime(input_number):
        print(f"{input_number} - простое число.")
    else:
        print(f"{input_number} - составное число.")
else:
    print("Число должно быть от 1 до 100000.")
