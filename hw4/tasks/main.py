# 🐀 Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# 🐀 Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# 🐀 Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# 🐀 При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# 🐀 В каждом решении нужно вывести время выполнения
# вычислений


from random import randint
import threading, multiprocessing, asyncio, time


start = time.time()
arr = [randint(1, 100) for _ in range(10**6)]
sum_ = 0
def sum_num(num_list):
    global sum_
    for i in num_list:
        sum_+= i

threadings = []
for i in range(10):
    start_ind = i * 100_000
    end_ind = start_ind + 100_000
    thread = threading.Thread(target=sum_num, args=(arr[start_ind:end_ind],))
    threadings.append(thread)

for thread in threadings:
    thread.start()

for thread in threadings:
    thread.join()

print(sum_) # 50491464
end = time.time()
print(end - start)  # 1.5673656463623047
