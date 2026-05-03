# def number_sum(n):
#     """Returns the sum of the first n numbers"""
#     assert n >= 0, "n must be >= 0"

#     if n == 0:
#         return 0
#     else:
#         return n + number_sum(n - 1)


# if __name__ == "__main__":
#     from timeit import Timer

#     t = Timer(
#         "number_sum(50)",
#         "from __main__ import number_sum",
#     )
#     print("Time: ", t.timeit())

# Цей варіант дуже повільний, тому спробуємо покращити його використовуючи декоратор



# Memoization


# sum_cache = {0: 0}
# def number_sum(n):
#     """Returns the sum of the first n numbers"""
#     assert n >= 0, "n must be >= 0"

#     if n in sum_cache:
#         return sum_cache[n]
#     res = n + number_sum(n - 1)
#     # Add the value to the cache
#     sum_cache[n] = res
#     return res

# if __name__ == "__main__":
#     from timeit import Timer

#     t = Timer(
#         "number_sum(300)",
#         "from __main__ import number_sum",
#     )
#     print("Time: ", t.timeit())

#Тут ми використали memoization - техніка збереження результатів для запобігання повторним обчисленням
#sum_cache - це місце звідки функція повертатиме значення, яке їх вже було відоме
#Для обчислення number_sum(100) ми б мусіли робити 100 кроків рекурсії
#Але якщо ми до того обраховували number_sum(99) то функція зробить лише 1 крок назад
#Але тут теж є свої проблеми. А якщо ми захочемо додати ще функцій і створити повноцінний модуль?

#fib_cache = {0: 0, 1: 1}

# def fibonacci(n):
#     """Returns the suite of Fibonacci numbers"""

#     if n in fib_cache:
#         return fib_cache[n]

#     res = fibonacci(n - 1) + fibonacci(n - 2)
#     fib_cache[n] = res
#     return res

#Ось що б нам довелось додати для обчислення чисел Фібоначчі
#Тут в нас зʼявляється нова змінна для того самого кешу
#Та й функція складніша ніж без memoizatino



# Decorator pattern

import functools


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def memoizer(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoizer

@memoize
def number_sum(n):
    """Returns the sum of the first n numbers"""
    if n == 0:
        return 0
    else:
        return n + number_sum(n - 1)

@memoize
def fibonacci(n):
    """Returns the suite of Fibonacci numbers"""
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    from timeit import Timer

    to_execute = [
        (
            number_sum,
            Timer(
                "number_sum(300)",
                "from __main__ import number_sum",
            ),
        ),
        (
            fibonacci,
            Timer(
                "fibonacci(100)",
                "from __main__ import fibonacci",
            ),
        ),
    ]

    for item in to_execute:
        func = item[0]
        print(
            f'Function "{func.__name__}": {func.__doc__}'
        )
        t = item[1]
        print(f"Time: {t.timeit()}")
        print()


if __name__ == "__main__":
    main()

#Тут ми все ще використовуємо memoixation, але робимо це розумно
#Замість повторювання коду ми створюємо функцію яка буде займатись збереженням
#А функції обчислення ми зробили звичайними (такими як в першому прикладі)
#Таким чином ми поєднали і простоту коду і його ефективність
