from external_adapter import Musician, Dancer

class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"the club {self.name}"

    def organize_event(self):
        return "hires an artist to perform"


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [
        Club("Jazz Cafe"),
        Musician("Roy Ayers"),
        Dancer("Shane Sparks"),
    ]

    for obj in objects:
        if hasattr(obj, "play") or hasattr(obj, "dance"):
            if hasattr(obj, "play"):
                adapted_methods = dict(
                    organize_event=obj.play
                )
            elif hasattr(obj, "dance"):
                adapted_methods = dict(
                    organize_event=obj.dance
                )

            # referencing the adapted object here
            obj = Adapter(obj, adapted_methods)

        print(f"{obj} {obj.organize_event()}")


if __name__ == "__main__":
    main()

#Нехай наш клуб хоче урізноманітнити свої вечірки і думає як це зроюити
#Колись клуб міг тільки organize_event
#Ми знайшли в інтернеті цікавий файл з музикантами і танцівниками (external_adapter.py)
#Але вони обоє не знають що таке oranize_event, тільки play() і dance() відповідно
#То ж як нам оновити код без зміни цих двох класів? Створити Adapter!
#Всередині адаптера ми зберігаємо obj - музиканта, танцбриста чи звичайний обʼєкь клубу
#В __dict__ зберігаються всі методи та атрибути кожного класу, а отже і нашого obj
#.update() бере елементи __dict__ і вписує їх в інший (organize_evenr = play)
#Тепер кожен клас знає що таке organize_event і може його використовувати

