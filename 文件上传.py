
from fastapi import FastAPI, File

app = FastAPI()


# 小文件上传
@app.post("/upload1")
def file_upload1(file: bytes = File(...) ):
    # 写数据
    with open("./image/picture1", "wb") as f:
        f.write(file)
    return {"msg": "文件上传成功"}