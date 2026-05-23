# import threading
# import requests
# import time


# def download(url):
#     print(f"Starting download from {url}")
#     resp = requests.get(url)
#     print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")


# urls = [
#     "https://www.bing.com/th/id/OIP.qbBzNxn0pvjT6aAklZDvwwHaNK?w=238&h=424&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2",
#     "https://www.bing.com/th/id/OIP.d85uClRgp9jfl2lz288dGwHaFx?w=296&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2",
#     "https://th.bing.com/th?id=ONUT.bEVjRtAPX35Pd6d9LWEvoQ&pid=News&w=316&h=200&c=14&rs=2&qlt=90&dpr=1.5",
#     "https://www.bing.com/th/id/OIP.2dPXv2RH3LVvFcOtNU7RfAHaE7?w=190&h=128&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2",
#     "https://www.bing.com/th/id/OIP.Ggvs4sbza3sZPNhGPem-zwHaHa?w=126&h=128&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2",
# ]


# start = time.time()
# threads = []
# for url in urls:
#     t = threading.Thread(target=download, args=(url,))
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# end = time.time()
# print(f"All downloads done in {end - start:.2f} seconds")










