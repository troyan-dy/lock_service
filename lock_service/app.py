import asyncio
from typing import Any, Dict

import uvicorn
from fastapi import APIRouter, FastAPI

api_router = APIRouter()


LOCKS: Dict[str, Any] = {}


@api_router.post("/take")
async def take_lock(key: str) -> bool:
    if key in LOCKS:
        await LOCKS[key].wait()
    else:
        LOCKS[key] = asyncio.Event()
    return True


@api_router.post("/put")
async def put_lock(key: str) -> bool:
    if key in LOCKS:
        LOCKS[key].set()
        del LOCKS[key]
    return True


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
