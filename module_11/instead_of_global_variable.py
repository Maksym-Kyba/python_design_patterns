# counter = 0
# def increment():
#     global counter
#     counter += 1
# def reset():
#     global counter
#     counter = 0

class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0


if __name__ == "__main__":
    c = Counter()
    print(f"Counter value: {c.counter}")
    c.increment()
    print(f"Counter value: {c.counter}")
    c.reset()
