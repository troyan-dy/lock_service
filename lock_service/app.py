import asyncio
import os
from typing import Any, Dict

import uvicorn
from fastapi import APIRouter, FastAPI

api_router = APIRouter()


DEFAULT_PORT = 5000

LOCKS: Dict[str, Any] = {}  # noqa: WPS407 -- in-memory lock registry is the service state


@api_router.post("/take")
async def take_lock(key: str) -> bool:
    event = LOCKS.get(key)
    if event is None:
        LOCKS[key] = asyncio.Event()
    else:
        await event.wait()
    return True


@api_router.post("/put")
async def put_lock(key: str) -> bool:
    event = LOCKS.pop(key, None)
    if event is not None:
        event.set()
    return True


def create_app() -> FastAPI:
    app = FastAPI(title="Lock service")
    app.include_router(api_router)
    return app


app = create_app()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    uvicorn.run(app=app, host="0.0.0.0", port=port)
