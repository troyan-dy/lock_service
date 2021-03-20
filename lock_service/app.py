from typing import Optional

import uvicorn
from fastapi import APIRouter, FastAPI

api_router = APIRouter()


@api_router.get("/lock")
async def get_lock(key: str, expire: Optional[int] = None):
    return True


@api_router.delete("/lock")
async def remove_lock(key: str):
    return True


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
