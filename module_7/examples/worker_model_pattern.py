from multiprocessing import Process, Queue
import time


def worker(task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        print(f"Worker {task} is processing")
        time.sleep(1)
        print(f"Worker {task} completed")


def main():
    task_queue = Queue()

    # Populate the task queue
    for i in range(10):
        task_queue.put(i)

    # Create 5 worker processes
    processes = [
        Process(target=worker, args=(task_queue,))
        for _ in range(5)
    ]

    # Start the worker processes
    for p in processes:
        p.start()

    # Wait for all worker processes to finish
    for p in processes:
        p.join()

    print("All tasks completed.")


if __name__ == "__main__":
    main()

#В нас є task_queue яка зберігає завдання і чекає поки їх виконають
#processes це наші робітники. Кожен бере собі завдання з черги і робить
#Потім вони беруть ще завдання за потреби
#worker це така собі інструкція за якою працюють наші робітники

#Це дуже схоже на Thread Pool але я декілька відмінностей
#1) В Thread Pool всі разом бачать одні й ті самі змінні, а наші воркери незалежні і не бачать памʼять один одного
#2) Якщо якийсь thread впаде то впадуть всі, а воркери можуть працювати далі
#3) Воркери працюють одночасно
#Також воркери можуть юути різними серверами (це помагає в Serverless та Microservices patterns)

