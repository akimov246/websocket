import asyncio

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.5)

async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_nums())
    #taks2 = asyncio.create_task(print_time())

    #await asyncio.gather(task1, taks2)
    await asyncio.gather(task1)

if __name__ == '__main__':
    asyncio.run(main())