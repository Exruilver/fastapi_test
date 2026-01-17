from fastapi import FastAPI, Path, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


# 基础方式
@app.post("/login1")
def login1(username: str = Form(), password : int = Form()):
    return {"用户名": username, "密码": password}



# 第二种方式
class User2(BaseModel):
    username: str
    password: int
# 
@app.post("/login2")
def login2(user: Annotated[User2, Form()]):
    return user



# 第三种方式
class User3(BaseModel):
    username: str = Form(...)
    password: int = Form(...)
# 
@app.post("/login3")
def login3(user: Annotated[User3, Form()]):
    return user
