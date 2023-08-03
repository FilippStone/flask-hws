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
arr = [randint(1, 100) for _ in range(10 ** 6)]
sum_ = multiprocessing.Value('i', 0)


def sum_num(num_list, sum_):
    for i in num_list:
        with sum_.get_lock():
            sum_.value += i



if __name__ == '__main__':
    procesess = []
    for i in range(10):
        start_ind = i * 100_000
        end_ind = start_ind + 100_000
        proceses = multiprocessing.Process(target=sum_num, args=(arr[start_ind:end_ind], sum_))
        procesess.append(proceses)

    for proceses in procesess:
        proceses.start()

    for proceses_1 in procesess:
        proceses_1.join()

    print(sum_.value) # 50492361
    end = time.time()
    print(end - start) # 20.404144048690796
