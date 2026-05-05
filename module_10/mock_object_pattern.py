import unittest
from unittest.mock import mock_open, patch


class Logger:
    def __init__(self, filepath):
        self.filepath = filepath

    def log(self, message):
        with open(self.filepath, "a") as file:
            file.write(f"{message}\n")


class TestLogger(unittest.TestCase):
    def test_log(self):
        msg = "Hello, logging world!"

        m_open = mock_open()

        with patch("builtins.open", m_open):
            logger = Logger("dummy.log")
            logger.log(msg)

            m_open.assert_called_once_with(
                "dummy.log", "a"
            )
            m_open().write.assert_called_once_with(
                f"{msg}\n"
            )


if __name__ == "__main__":
    unittest.main()

#Ми хочемо протестувати Logger
#Зазвичай наш Logger створює файл, але ми не хочемо засоряти собі комп
#Саме тут потрібен Mock Object Pattern
#Ми створюємо якийсь mock обʼєкт який імітуватиме наш
#В нашому випадку ми робимо це через mpck_open() який лише імітує відкриття файлу
#patch("builtins.open", m_open) - це наша заміна
#Вона роюбить так щоб open виконувалась але не чіпала жорсткий диск
#А далі ми просто тестимо як завжди

