import asyncio
import time 

# The event loops helps in taking orders from
# multiple users or helps in managing several requests 
# at a time.
# so what the event loop does is that it 
# takes a request from one user and then while in that server
# or while executing that action it checks 
# if there's another request. So it waits there while taking 
# other requests but returns the results for the previous 
# or earlier requests. That's why it takes some few seconds to get 
# your result. It does or allows for waiting but without blocking the 
# if we had used multithreading or multiprocessing, the
# results would have been blocked


async def brew(name):
    print(f"Brewing {name}....")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f"{name} is ready!")


async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai")
        
    )



























