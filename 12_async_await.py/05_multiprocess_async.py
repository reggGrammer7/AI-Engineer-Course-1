import asyncio
from concurrent.futures import ProcessPoolExecutor


# What it means:“Hey asyncio, don’t run encrypt() here.”

# “Send it to a separate process.”

# “Let that process run it.”

# “When it finishes, give me the result.”


def encrypt(data):
    return f"🔏 lcoked data{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result =await loop.run_in_executor(pool,encrypt,"credit_card_1234")
        print(f"{result}")



if __name__ == "__main__":
    asyncio.run(main())


# Because if you run CPU work inside asyncio: It blocks the event loop
# No other async tasks can run Your app freezes





























