quotes = (
    "A man is not complete until he is married. Then he is finished.",
    "As I said before, I never repeat myself.",
    "Behind a successful man is an exhausted woman.",
    "Black holes really suck...",
    "Facts are stubborn things.",
)


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = "Not found!"
        return value


class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f"Error: {msg}")

    def select_quote(self):
        return input("Which quote number would you like to see? ")


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == "__main__":
    main()

#Головна ідея це розділити виконання програми між трьома виконувачами
#Model відповідає лише за дані, які десь зберігаються і вона має до них доступ
#Але модель взагалі не знає хто її і як використовує
#Далі є View - він відповідає за відображення і виведення даних/помилок
#Але View не знає про існування цитат і про існування юзера
#Controller сполучає користувача й View з Model
#Тоюто разом ці три класи утворюють повноцінну програму (один знає одне інший інше)

