from eventsourcing.domain import Aggregate, event
from eventsourcing.application import Application


class InventoryItem(Aggregate):
    @event("ItemCreated")
    def __init__(self, name, quantity=0):
        self.name = name
        self.quantity = quantity

    @event("QuantityIncreased")
    def increase_quantity(self, amount):
        self.quantity += amount

    @event("QuantityDecreased")
    def decrease_quantity(self, amount):
        self.quantity -= amount


class InventoryApp(Application):
    def create_item(self, name, quantity):
        item = InventoryItem(name, quantity)
        self.save(item)
        return item.id

    def increase_item_quantity(self, item_id, amount):
        item = self.repository.get(item_id)
        item.increase_quantity(amount)
        self.save(item)

    def decrease_item_quantity(self, item_id, amount):
        item = self.repository.get(item_id)
        item.decrease_quantity(amount)
        self.save(item)


def main():
    app = InventoryApp()

    # Create a new item
    item_id = app.create_item("Laptop", 10)
    # Increase quantity
    app.increase_item_quantity(item_id, 5)
    # Decrease quantity
    app.decrease_item_quantity(item_id, 3)

    notifs = app.notification_log.select(start=1, limit=5)
    notifs = [notif.state for notif in notifs]
    for notif in notifs:
        print(notif.decode())


if __name__ == "__main__":
    main()

#Aggregate - це обʼєкт, чий стан ми відстежуємо
#Щоразу як викликається метод з декоратором @event бібліотека створює запис у журналі (даючи попередньо мітку)
#В InventoryApp Repository це місце де зберішаються події (уявимо що це база даних)
#self.save записує в базу всі події які сталися

#Коли ми робимо increase_item_quantity ми записуємо цю зміну собі в базу даних
#Переваги тут ті ж самі - аудит, відтворення старих станів
