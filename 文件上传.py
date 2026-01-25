import aiofiles
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# 小文件上传
@app.post("/upload1")
def file_upload1(file: bytes = File(...) ):
    # 写数据
    with open("./image/picture1.jpg", "wb") as f:
        f.write(file)
    return {"msg": "文件上传成功"}


# # 上传大文件
# @app.post("/upload2")
# def file_upload2(file: UploadFile):
#     # 写数据
#     with open(f"./image/{file.filename}", "wb") as f:
#         # 注意这里 f.write 方法接受的是字节数据，不能传入 UploadFile 对象
#         f.write(file)
#     return {"msg": "文件上传成功"}

# 上面这种写法是错误的



#========================================                 上传大文件使用异步文件操作                    ========================================


@app.post("/upload2")
async def file_upload2(file: UploadFile):
    # 写数据
    async with aiofiles.open("./image/picture2.jpg", "wb") as f:
        context = await file.read(1024*1024)

        while context:

            f.write(context)
            context = await file.read(1024*1024)
            

    return {"msg": "文件上传成功"}




#========================================                      以下内容皆为注释                        ========================================


# 如果是上传文件的接口 http 请求的 Content-Type 必须是 multipart/form-data
# 如果是表单的接口 http 请求的 Content-Type 可以是 application/x-www-form-urlencoded 也可以是 multipart/form-data
# 如果接口时普通的 json 接口 http 请求的 Content-Type 必须是 application/json