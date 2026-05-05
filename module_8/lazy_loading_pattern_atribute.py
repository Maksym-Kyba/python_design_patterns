class LazyLoadedData:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = self.load_data()
        return self._data

    def load_data(self):
        print("Loading expensive data...")
        return sum(i * i for i in range(100000))


def main():
    obj = LazyLoadedData()
    print("Object created, expensive attribute not loaded yet.")

    # The expensive operation will occur only when the attribute is accessed for the first time
    print("Accessing expensive attribute:")
    print(obj.data)
    print("Accessing expensive attribute again, no reloading occurs:")
    print(obj.data)


if __name__ == "__main__":
    main()

#При ініціалізації обʼєкта ми просто підставили замість складних даних None
#Логіку з @property ми додали, щоб коли був запит на доступ до даних, була логіка їх завантаження
#Якщо ж дані вже доводилось завантажувати то нічого заново не вантажиться
#Це дозвляє сильно зменшити затрати та використання ресурсів

#The lazy loading pattern, applied this way, is very useful for improving performance
#In applications where certain data or computations are needed from time to time
#But are expensive to produce.
