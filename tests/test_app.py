import asyncio

import pytest
from async_timeout import timeout


@pytest.mark.asyncio
async def test_timeout(client):
    await client.post("/take?key=123")
    with pytest.raises(asyncio.TimeoutError):
        async with timeout(1):
            await client.post("/take?key=123")


@pytest.mark.asyncio
async def test_correct_work(client):
    try:
        async with timeout(2):
            await client.post("/take?key=222")
            await client.post("/put?key=222")
            await client.post("/take?key=222")
    except asyncio.TimeoutError:
        assert False, "Got unexpected timeout"
