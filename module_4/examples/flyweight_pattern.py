import random
from enum import Enum

CarType = Enum(
    "CarType", "SUBCOMPACT COMPACT SUV"
)


class Car:
    pool = dict()

    def __new__(cls, car_type):
        obj = cls.pool.get(car_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        type = self.car_type
        msg = f"render a {color} {type.name} car at ({x}, {y})"
        print(msg)


def main():
    rnd = random.Random()
    colors = [
        "white",
        "black",
        "silver",
        "gray",
        "red",
        "blue",
        "brown",
        "beige",
        "yellow",
        "green",
    ]
    min_point, max_point = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarType.SUBCOMPACT)
        c1.render(
            random.choice(colors),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point),
        )
        car_counter += 1

    for _ in range(3):
        c2 = Car(CarType.COMPACT)
        c2.render(
            random.choice(colors),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point),
        )
        car_counter += 1

    for _ in range(5):
        c3 = Car(CarType.SUV)
        c3.render(
            random.choice(colors),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point),
        )
        car_counter += 1

    print(f"cars rendered: {car_counter}")
    print(
        f"cars actually created: {len(Car.pool)}"
    )

    c4 = Car(CarType.SUBCOMPACT)
    c5 = Car(CarType.SUBCOMPACT)
    c6 = Car(CarType.SUV)
    print(
        f"{id(c4)} == {id(c5)}? {id(c4) == id(c5)}"
    )
    print(
        f"{id(c5)} == {id(c6)}? {id(c5) == id(c6)}"
    )


if __name__ == "__main__":
    main()

#Уявімо що ми хочемо зарендерити дуже дуже багато машин
#У машин є типи, які ми продумали раніше і надали кожному типу м=певні характеристики
#Але користувач також може кастомізувати частину характеристик (колір і координати спавну)
#В такому випадку ми будемо рендерити лише три обʼєкти (3 різні типи машин), просто з різними кастомними характеристиками
#Це дуже сильно зменшує навантаження на памʼять

#В __new__ ми дивимось чи існує вже обʼєкт для певного типу машини
#Якщо так то ми повертаємо посилання на вже існуючий обʼєкт і даємо йому кастомні характеристики
#Проте після створення в нс ніде не зберішається колір, ми його використали, створили і заюули
#На локації згенерувалась жовта машина і нам вже ніколи не доведеться міняти колір, тому ми перевикористовуємо її на синю машинуА

#__new__ по дефолту відповідає за створення обʼєкта, але тут ми його трішки змінили
#Це зроблено, щоб не створювати обʼєкт щоразу, а перевикористовувати його
