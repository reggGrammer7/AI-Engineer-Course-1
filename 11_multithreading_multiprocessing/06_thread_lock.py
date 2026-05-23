# Locks ensure only one thread modifies a given
# variable at a time 
# Mostly used when you are accessing a global
# variable 


import threading
counter = 0
lock = threading.Lock()

def increment():
    global counter 
    for _ in range(10000):
        with lock:
            counter += 1

threads = [threading.Thread(target= increment) for _ in range(10)]
[t.start() for t  in threads]
[t.join() for t  in threads]

print(f"FInal Counter: {counter}")
