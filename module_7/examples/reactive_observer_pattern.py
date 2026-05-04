from pathlib import Path
import reactivex as rx
from reactivex import operators as ops


def firstnames_from_db(path: Path):
    file = path.open()

    # collect and push stored people firstnames
    return rx.from_iterable(file).pipe(
        ops.flat_map(
            lambda content: rx.from_iterable(
                content.split(", ")
            )
        ),
        ops.filter(lambda name: name != ""),
        ops.map(lambda name: name.split()[0]),
        ops.group_by(lambda firstname: firstname),
        ops.flat_map(
            lambda grp: grp.pipe(
                ops.count(),
                ops.map(lambda ct: (grp.key, ct)),
            )
        ),
    )


def main():
    db_path = Path(__file__).parent / Path("people.txt")

    # Emit data every 5 seconds
    rx.interval(5.0).pipe(
        ops.flat_map(lambda i: firstnames_from_db(db_path))
    ).subscribe(lambda val: print(str(val)))

    # Keep alive until user presses any key
    input("Starting... Press any key and ENTER, to quit\n")


if __name__ == "__main__":
    main()

#rx.from_iterable(file) перетворює рядки з файлу на потік даних.
#ops.flat_map(...) розбиває рядки на окремі імена (якщо в рядку кілька імен через кому).
#ops.filter(...) викидає порожні рядки.
#ops.map(...) бере лише ім'я (відкидає прізвище).
#ps.group_by та ops.count групують однакові імена та рахують, скільки разів кожне з них зустрілося.

#rx.interval(5.0) - це наше Observable.
#Кожні 5 секунд воно "дзвонить у дзвоник" і запускає весь процес заново.
#subscribe(lambda val: print(val)) це і є момент реалізації Observer
#Поки ми не викликали subscribe, код вище — це просто "схема", яка нічого не робить.
#Як тільки ми підписалися дані пішли і ми почали їх друкувати.

#Якщо безпосередньо під час виконання програми змінити вміст файлу то воно почне його обробляти
#Наш Observer спостерінає за потоком даних з файлу
#Кожні 5 секунд ми дивимось у файл і якщо шось змінилось то наступний раз спостерігач (lambda print) обробить це

#Поки відбуваються ці інтервали потік решти програми триває
