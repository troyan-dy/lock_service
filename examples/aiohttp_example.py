import asyncio
from contextlib import asynccontextmanager

import aiohttp


@asynccontextmanager
async def distributed_locking(name: str):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://0.0.0.0:5000/take", params={"key": name}):
            print(f"Take lock '{name}'")
            yield
        async with session.post("http://0.0.0.0:5000/put", params={"key": name}):
            print(f"Put lock '{name}'")


async def task_to_be_blocked(lock_name: str, task_name: str):
    print(f"start {task_name}")
    async with distributed_locking(name=lock_name):
        print(f"start do job at {task_name}")
        await asyncio.sleep(3)
        print(f"finish do job at {task_name}")


async def main():
    coros = [
        task_to_be_blocked(lock_name="any_lock", task_name="Task 1"),
        task_to_be_blocked(lock_name="any_lock", task_name="Task 2"),
    ]
    await asyncio.gather(*coros)


if __name__ == "__main__":
    asyncio.run(main())
