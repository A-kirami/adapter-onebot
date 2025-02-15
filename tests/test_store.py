import asyncio

import pytest


@pytest.mark.asyncio
async def test_store():
    from nonebot.adapters.onebot.store import ResultStore

    store = ResultStore()

    seq = store.get_seq()
    data = {"test": "test"}
    response_data = {
        "status": "success",
        "retcode": 0,
        "data": data,
        "echo": str(seq),
    }

    async def feed_result():
        store.add_result(response_data)

    asyncio.create_task(feed_result())
    resp = await store.fetch(seq, 10.0)
    assert resp == response_data
