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
async def sum_num(num_list):
    global sum_
    for i in num_list:
        sum_+= i

tasks = []
async def main():
    sum_result = await sum_num(arr)

loop = asyncio.get_event_loop()
asyncio.run(main())

print(sum_) # 50531136
end = time.time()
print(end - start) # 1.7629034519195557
