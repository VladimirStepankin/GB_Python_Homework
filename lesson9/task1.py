import functools
import json
import math
import random
import csv


def quadratic_roots(a, b, c):
    """Функция нахождения корней квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root1 = root2 = -b / (2 * a)
        return root1, root2
    else:
        return None  # Корней нет


def generate_csv_file(filename, num_rows):
    """Генерация csv файла с 3-мя случайными числами в каждой строке"""
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            csv_writer.writerow(row)


def quadratic_roots_decorator(func):
    """Декоратор, запускающий фенкцию quadratic_roots"""

    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                a, b, c = map(float, row)
                roots = func(a, b, c)
                print(f"Корни для a={a}, b={b}, c={c}: {roots}")

    return wrapper


def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "args": args,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return result
        return wrapper
    return decorator


@quadratic_roots_decorator
@save_to_json("results.json")
def find_quadratic_roots(a, b, c):
    return quadratic_roots(a, b, c)


generate_csv_file("random_numbers.csv", 100)
find_quadratic_roots("random_numbers.csv")
