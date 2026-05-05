from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "10 per hour"],
    storage_uri="memory://",
    strategy="fixed-window",
)


@app.route("/limited")
def limited_api():
    return "Welcome to our API!"


@app.route("/more_limited")
@limiter.limit("2/minute")
def more_limited_api():
    return "Welcome to our expensive, thus very limited, API!"


if __name__ == "__main__":
    app.run(debug=True)


#В цьому коді роль обмежувача бере на себе бібліотека Limiter а саме flask_limiter
#get_remote_address: Лімітер ідентифікує користувача за його IP-адресою. Кожен IP має свій власний "лічильник".
#default_limits: Це загальні правила для всього сайту.
#strategy="fixed-window": Це метод підрахунку. Час ділиться на фіксовані відрізки
#Наприклад, з 12:00 до 13:00). Як тільки ти зробив 10 запитів у цьому вікні, наступні будуть заблоковані до 13:00.
#@app.route("/limited") накладає стандартні обмеження з лімітера
#@limiter.limit("2/minute") - цей накладає обмеження на конкретну функцію, яку декорує
#Якщо б ми перейшли на сайт і оновили його 10 разів, то ми б побачили, що забагато реквесиів

#Переваши цього патерну наступні
#Захист від DDoS атак: неможливо надсилати мільйони запитів дуже швидко
#Розподіл ресурсів рівномірніший, бо 1 користувач не може все зайняти
