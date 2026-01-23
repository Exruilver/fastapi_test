from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()



# 基础用法
@app.get("/file1")
def get_file1():
    file_path = "./image/picture1.jpg"  
    return FileResponse(path=file_path)
    # 或者写作 return FileResponse(file_path)

