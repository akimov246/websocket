import asyncio
import aiohttp
import requests
import time

# Синхронный стиль (выполняется примерно за 6-7 секунд)
# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
# def write_file(response: requests.Response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#
# def main():
#     t0 = time.time()
#     url = 'https://loremflickr.com/320/240'
#     for i in range(10):
#         write_file(get_file(url))
#     print(time.time() - t0)

# Асинхронный стиль

def write_image(data):
    filename = f'file-{int(time.time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)

async def fetch_content(url, session: aiohttp.ClientSession):
    async with session.get(url, allow_redirects = True) as response:
        data = await response.read()
        write_image(data)

async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time.time()
    #main()
    asyncio.run(main())
    print(time.time() - t0)

