# lock_service
http lock service

Ready for heroku

## Dependencies
- docker-compose
- python 3.14

## Commands
### Install
- `make install`

### Run tests
- `make test`
### Linting
- `make lint`

### Formatting
- `make format`

### Start in docker
- `make start`
- `make stop`


## Usage

- take lock
```bash
curl -X POST http://0.0.0.0:8000/take?key=123
```

- put lock
```bash
curl -X POST http://0.0.0.0:8000/put?key=123
```

## Example with aiohttp

```python
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

```
- Output
```bash
start Task 1
start Task 2
Take lock 'any_lock'
start do job at Task 1
finish do job at Task 1
Put lock 'any_lock'
Take lock 'any_lock'
start do job at Task 2
finish do job at Task 2
Put lock 'any_lock'
```
