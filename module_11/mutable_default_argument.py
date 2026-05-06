def manipulate(mylist=[]):
    mylist.append("test")
    return mylist


def better_manipulate(mylist=None):
    if not mylist:
        mylist = []

    mylist.append("test")
    return mylist


if __name__ == "__main__":
    print("function manipulate()")
    print(manipulate())
    print(manipulate())
    print(manipulate())

    print("function better_manipulate()")
    print(better_manipulate())
    print(better_manipulate())

#Коли Python бачить mylist=[], він створює один-єдиний список у пам'яті та "приклеює" його до функції.
#Тепер кожен наступний виклик функції використовує той самий об'єкт списку.
#Але такого не відбувається з None, бо це незмінюваний тип даних

