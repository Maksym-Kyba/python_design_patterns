from datetime import timedelta
from functools import lru_cache


def fibonacci_func1(n):
    if n < 2:
        return n
    return fibonacci_func1(n - 1) + fibonacci_func1(n - 2)


@lru_cache(maxsize=None)
def fibonacci_func2(n):
    if n < 2:
        return n
    return fibonacci_func2(n - 1) + fibonacci_func2(n - 2)


def main():
    import time

    n = 30

    start_time = time.time()
    result = fibonacci_func1(n)
    duration = timedelta(time.time() - start_time)
    print(f"Fibonacci_func1({n}) = {result}, calculated in {duration}")

    start_time = time.time()
    result = fibonacci_func2(n)
    duration = timedelta(time.time() - start_time)
    print(f"Fibonacci_func2({n}) = {result}, calculated in {duration}")


if __name__ == "__main__":
    main()

#Проблема першої функції в тому, що кожна рекурсія кожен раз по сто разів обчислює базові значення (наприклад 5)
#Друга функція використовує мемоїзацію (реалізовану через декоратор @lru_cache)
#Тепер 1 раз обчисливши 5 ми будемо зразу знати його значення і так для будь якого числа
#Дані мемоїзації лежать у самій програмі (В Cache-Aside це часто інший сервер)
