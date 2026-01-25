from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

# 在 http 请求中，如果我们要传输的数据不是 json 格式的而是表单类型的数据，
# 那么就需要用到 Form 了

app = FastAPI()


# 基础方式
# 下面使用 Form，用法和 Field、Query、Path 类似
@app.post("/login1")
def login1(username: str = Form(), password : int = Form()):
    return {"用户名": username, "密码": password}



# 第二种方式
class User2(BaseModel):
    username: str
    password: int


@app.post("/login2")
def login2(user: Annotated[User2, Form()]):
    return user



# 第三种方式
class User3(BaseModel):
    username: str = Form(...)
    password: int = Form(...)


@app.post("/login3")
def login3(user: Annotated[User3, Form()]):
    return user
