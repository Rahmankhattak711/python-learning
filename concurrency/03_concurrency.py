import threading
import requests
import time


def download(url):
    print(f"start downloading {url}")
    res = requests.get(url)
    print(f"finish downloading {url}")


images_urls = [
    "https://images.pexels.com/photos/140285/pexels-photo-140285.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
    "https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940",
]

start = time.time()

threads = []
for url in images_urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"Time taken: {end - start:.2f} seconds")
