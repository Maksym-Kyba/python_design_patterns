from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    print(f"Executing task {n}")
    time.sleep(1)
    print(f"Task {n} completed")


with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks to the thread pool
    for i in range(10):
        executor.submit(task, i)

#Головна ідея це створити певну кількість "виконавців завдань" (Threads) щоб не створювати їх кожного разу
#Коли хтось з виконувачів звідбняється він чекає на наступне завдання і починає його виконувати
#Чимось це схоже на Object Pool Pattern
