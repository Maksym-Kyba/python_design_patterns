class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print(f"function overriden: {self.method}")
        # print(f"function's name: {self.method_name}")

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        # print(f'value {value}')
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = "foo"
        self.y = "bar"
        self._resource = None

    @LazyProperty
    def resource(self):
        print("initializing self._resource...")
        print(f"... which is: {self._resource}")
        self._resource = tuple(range(5))  # expensive
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # do more work...
    print(t.resource)
    print(t.resource)


if __name__ == "__main__":
    main()

#Тут Proxy слугує як замінник реального значення
#resource не обчислюється і не створюється поки він нам не знадобиться, тому він просто None
#Коли він нам знадобився, створюється екзмепляр класу LazyProperty (бо цей клас слугує декоратором)
#__get__ запускаж оригінальний метод value = ... і setattr перезаписує значення обʼєкту
#Другий раз це все не відбувається, бо ми вже обрахували значення resource при першій потреюі
#Це може зекономити ресурси, якщо обчислення дуже громіздке, а атрибут навіть не знадобиться
