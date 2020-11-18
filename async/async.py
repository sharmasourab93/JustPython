import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(10)
    print("World")
    

if __name__ == '__main__':
    asyncio.run(main())
