# Field 是用来对请求体参数进行更详细的验证和配置的

from fastapi import FastAPI
from pydantic import Field,BaseModel

app = FastAPI()





# 默认值和必填字段校验
class Item(BaseModel):
    name: str = Field(default="化学必修三")
    id: int = Field(...)

@app.post("/items/")
def read_item1(item: Item):
    return item



# 字符串长度校验和数值大小校验以及正则表达式校验
class Item(BaseModel):
    name: str = Field(min_length=3, max_length=100, pattern=r"^[a-zA-Z0-9\s]+$")
    # 这里正则表达式的含义是只允许字母、数字和空白字符
    # 其中，+ 表示前面的字符可以出现一次或多次，
    # \s 表示空白字符

    id: int = Field(..., ge=1, le=1000)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    # 这里的正则表达式用于简单的邮箱格式校验
    # 其中，+ 表示前面的字符可以出现一次或多次，
    # \. 表示邮箱格式中的点号
    # {2,} 表示前面的字符至少出现两次，上不封顶



@app.post("/books/")
def read_item1(book: Item):
    return book