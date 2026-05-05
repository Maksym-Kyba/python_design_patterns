import pybreaker
from datetime import datetime
import random
from time import sleep


breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=5)


@breaker
def fragile_function():
    if not random.choice([True, False]):
        print(" / OK", end="")
    else:
        print(" / FAIL", end="")
        raise Exception("This is a sample Exception")


def main():
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end="")

        try:
            fragile_function()
        except Exception as e:
            print(" / {} {}".format(type(e), e), end="")
        finally:
            print("")
            sleep(1)


if __name__ == "__main__":
    main()

#Уявімо, що наша функція дуже нестійка через дуже поганий звʼязок
#Саме для цього ми і будемо застосовувати Circuit Braker Pattern та бібліотеку pybreaker
#breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=5) - це нащ запобіжник
#Якщо будек дві помилки підряд, то на 5 секунд будь-яка спроба викликати функцію
#Викличе помилку (навіть без виклику функції)
#Після 5 спроб брейкер дасть ще спроби і знову зупинить якщо спроби будуть невдалі

#Може здатись що це просто краща версія Retry але це трішки не так
#Retry працює на рівні одного користувача і буде давати йому ше шанси
#Коли Circuit Breaker помітить шо Retry дає забагато шансів, він заблокує доступ усім а не лише 1 користувачу
