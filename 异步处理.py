import asyncio, time
from fastapi import FastAPI


app = FastAPI()


@app.get("/async")
async def async_endpoint():
    start = time.time()
    # 模拟 5 次异步 I/O  操作（并发执行）
    tasks = [asyncio.sleep(1) for _ in range(5)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"异步时长": f"{end - start:.2f}秒"}



@app.get("/sync")
def sync_endpoint():
    start = time.time()
    # 模拟 5 次同步 I/O 操作（顺序执行）
    for _ in range(5):
        time.sleep(1)
    end = time.time()
    return {"同步时长": f"{end - start:.2f}秒"}