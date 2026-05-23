# They are used to stop a thread from running
# when the main thread is done. They are used 
# when some loops are still running after the 
# main goal or achieved


import threading
import time 
def monitor_tea_time():
    while True:
        print(f"Monitoring tea temperature....")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_time,daemon=True)
t.start()
print("Main program done✅")
































