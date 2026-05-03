class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f"handle_{event}"
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, "handle_default"):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print(f"MainWindow: {event}")

    def handle_default(self, event):
        print(f"MainWindow Default: {event}")


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f"SendDialog: {event}")


class MsgText(Widget):
    def handle_down(self, event):
        print(f"MsgText: {event}")


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ("down", "paint", "unhandled", "close"):
        evt = Event(e)
        print(f"Sending event -{evt}- to MainWindow")
        mw.handle(evt)
        print(f"Sending event -{evt}- to SendDialog")
        sd.handle(evt)
        print(f"Sending event -{evt}- to MsgText")
        msg.handle(evt)


if __name__ == "__main__":
    main()

#Тут ми створюємо ланцюжок батьків (MainWindow -> SendDialog -> MsgText)
#Далі обʼєкт (наприклад mw) перевіряє чи є в нього певний handle (наприклад handle_point)
#Якщо є (hasattr) то цей метод просто виконується
#Якщо ні, то ми рухаємось по ланцюжку батьків поки не буде потрібного методу
#Якщо ніде не знайшовся потрібний метод, викликажться handle_default, якщо такий є
#Якщо і його нема то викликається handle з Widget (він батько для усіх)
#Це потрібно тоді коли ми точно не знаємо як буде оброблятись подія і ми її відправляємо плисти по течії поки виконувач не знайдеться
#Також це запобігає сотні if-else для перевірки який це клас щоб знати кому делегувати виконання
