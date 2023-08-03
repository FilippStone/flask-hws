"""Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле,
название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения
и общем времени выполнения программы.
"""
import requests

urls = ["https://free-images.com/lg/a31c/swan_flying_bird_fly.jpg",
        "https://free-images.com/lg/176d/squirrel_tail_bushy_tail.jpg",
        "https://free-images.com/lg/5c4e/mont_blanc_2005_118.jpg"]

def download_image(url, save_path):
    response = requests.get(url)
    for url in urls:
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
                print(f"Downloaded: {url} -> {save_path}")
        else:
            print(f"Failed to download: {url}")




