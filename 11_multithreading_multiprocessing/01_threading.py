# Concurrency is associated with threading and is the process
# whereby you allow each function to be working behind the scene
# all threaded functions or operators start at the same time 


# Parallelism 
# This is associated with multiprocessing such that each subsequent function'
# works one at a time. So one subsequent function or process only 
# starts or executes when the other is finished





import threading
import time

def take_orders():

    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2)




def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)


# create threads 
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")













