import threading, time, sys, os
from main import download_image


def download_with_threads(urls):
    start_time = time.time()

    threads = []
    for url in urls:
        file_name = url.split("/")[-1]
        save_path = os.path.join("downloads", file_name)
        thread = threading.Thread(target=download_image, args=(url, save_path))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time with threads: {total_time} seconds")
