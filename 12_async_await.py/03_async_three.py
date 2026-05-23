# # Fetching a web request 
# import asyncio
# import aiohttp


# async def fetch_url(session,url):
#     async with session.get(url) as response:
#         print(f"Fetched {url} with status {response.status}")


# async def main():
#     urls = ["https://httpbin.org/delay/2"] * 5
#     async with aiohttp.CleintSession() as session:
#         tasks = [fetch_url(session, url) for url in urls]
           # tasks = [t1,t2,t3] used because we will receive multipe requests

#         await asyncio.gather(*tasks)
            # await asyncio.gather(t1,t2,t3]

# asyncio.run(main())


# ASYNCIO exists because of blocking and non-blocking
# When someone is already 
















