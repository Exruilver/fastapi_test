from fastapi import FastAPI
from pydantic import BaseModel

class Fucker(BaseModel):
    name: str
    age: int
    email: str | None            # 设置可选参数如果不传则为 None，传入只能是字符串类型
    weight: float = 70.0 
    gender: str = '男'           # 设置类型注解并设置默认值为 男

app = FastAPI()



# 在这个函数中，是不支持对请求体参数进行数据校验的 ，如果我们字典中传入的数据类型不符合预期，程序也不会报错
# 比如这个字典中我写的是 age: "hello"，程序也不会报错
@app.post("/lover")
def lover_info(lover:dict):     # 传入的请求体参数是一个字典
    return lover                # 将接收到的请求体原封不动地返回



# 如果我们希望对请求体参数进行数据类型和数据格式的校验，可以使用 Pydantic 模型类来定义请求体参数
# 比如要对上面的 Fucker 类的 name 参数进行非空字符串校验，age 参数进行整数校验等
@app.post("/fucker2")
def manba_info(Fucker: Fucker):   # 传入的请求体参数是一个 Pydantic 模型类
    return Fucker

# pydantic 模型类定义的请求体参数会自动进行数据校验，如果传入的数据类型不符合预期，程序会报 422 错误