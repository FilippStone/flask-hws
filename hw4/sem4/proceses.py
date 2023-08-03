from main import download_image
import multiprocessing, time, sys, os

def download_with_processes(urls):
    start_time = time.time()

    processes = []
    for url in urls:
        file_name = url.split("/")[-1]
        save_path = os.path.join("downloads", file_name)
        process = multiprocessing.Process(target=download_image, args=(url, save_path))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time with processes: {total_time} seconds") #Downloaded: https://free-images.com/lg/5c4e/mont_blanc_2005_118.jpg -> downloads\swan_flying_bird_fly.jpg
    # Total time with processes: 2.8830618858337402 seconds

    download_with_processes(urls)
