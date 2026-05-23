# Global Interpreter Lock (GIL)
# This concept is mostly used in threading where 
# two threads try to access and change the value in 
# a memory location.
# To prevent two or threads issues python uses GIL to ensure 
# that one only one thread has access at a particular time 
# and that thread has what we call mutex which locks everything 
# or access to it. It is only when it is done that the other thread 
# can access the same memory location or value




#Threads: All threads appear to run at the same time,
#  but only one thread at a 
# time can execute Python bytecode because they all
#  share one GIL. All threads share the same memory space and the 
# same python interpreter and one GIL.There is GIL contention
# between threads. Good for I/O

# Processes: Each process has its own Python interpreter 
# and its own GIL, so they can truly run in parallel on 
# multiple CPU cores. Good for CPU
import threading 
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing")
    count = 0
    for _ in range(100_000_000):
        count +=1 
    print(f"{threading.current_thread().name} finished brewing")



thread1 = threading.Thread(target=brew_chai, name = "Barsita-1 ")
thread2 = threading.Thread(target=brew_chai, name = "Barsita-2 ")


start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print(f"Total time taken is: {end-start} seconds")




