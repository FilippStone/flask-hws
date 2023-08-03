from main import download_image
import asyncio, time, sys, os, requests


async def download_image_async(url, save_path):
    response = await loop.run_in_executor(None, requests.get, url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded: {url} -> {save_path}")
    else:
        print(f"Failed to download: {url}")

async def download_with_asyncio(urls):
    start_time = time.time()

    download_tasks = []
    for url in urls:
        file_name = url.split("/")[-1]
        save_path = os.path.join("downloads", file_name)
        download_task = download_image_async(url, save_path)
        download_tasks.append(download_task)

    await asyncio.gather(*download_tasks)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time with asyncio: {total_time} seconds") # Total time with asyncio: 3.465790033340454 seconds


if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Please provide a list of URLs as command line arguments.")
        sys.exit(1)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    loop = asyncio.get_event_loop()

    loop.run_until_complete(download_with_asyncio(urls))

    loop.close()
