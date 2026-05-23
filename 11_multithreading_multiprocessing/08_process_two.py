import threading
import time
from multiprocessing import Process

def cpu_heavy():
    print(f"Crunching some numbers....")
    total = 0 
    for i  in range(10**9):
        total += i
    print("Done ")

if __name__ == "__main__":
    start = time.time()

    processors = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processors]
    [t.join() for t in processors]

    print(f"Final time {time.time()- start:.2f} seconds ")


























