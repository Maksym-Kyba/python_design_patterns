from cowpy import cow


def generate_banner(msg, style):
    print("-- start of banner --")
    print(style(msg))
    print("-- end of banner --nn")


def dots_style(msg):
    msg = msg.capitalize()
    ten_dots = "." * 10
    msg = f"{ten_dots}{msg}{ten_dots}"
    return msg


def admire_style(msg):
    msg = msg.upper()
    return "!".join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def main():
    styles = (dots_style, admire_style, cow_style)
    msg = "happy coding"
    [generate_banner(msg, style) for style in styles]


if __name__ == "__main__":
    main()

#Тут приклад дещо не той бо зазвичай Template Pattern базується на класах а не на функціях
#Зокрема він базується на успадкуванні (базовий клас задає структуру, підкласи - деталі)
#Тут наш Template це start of banner i end of banner бо ця логіка має бути у всіх спільна
#Чимось це похоже на найпрсотіші варіанти використання декоратора


# class BannerGenerator: # Базовий клас-шаблон
#     def generate(self, msg):
#         print("-- start of banner --")
#         print(self.apply_style(msg)) -- Абстрактний крок
#         print("-- end of banner --")

#     def apply_style(self, msg):
#         raise NotImplementedError()

# class CowBanner(BannerGenerator): -- Конкретна реалізація
#     def apply_style(self, msg):
#         return cow.milk_random_cow(msg)

#Це дещо кращий приклад
