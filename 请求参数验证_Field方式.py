# Field 是用来对请求体参数进行更详细的验证和配置的
# Field 字段是需要写在定义的数据模型类中的
# 而不是直接写在函数的参数中

from fastapi import FastAPI
from pydantic import Field,BaseModel

app = FastAPI()





#######################             默认值和必填字段校验             #######################

class Item1(BaseModel):
    name: str = Field(default="化学必修三")
    id: int = Field(...)

@app.post("/items/")
def read_item1(item: Item1):
    return item



#######################             字符串长度校验和数值大小校验以及正则表达式校验             #######################
class Item2(BaseModel):
    name: str = Field(min_length=3, max_length=100, pattern=r"^[a-zA-Z0-9\s]+$")
    # 这里正则表达式的含义是只允许字母、数字和空白字符
    # 其中，+ 表示前面的字符可以出现一次或多次，
    # \s 表示空白字符

    id: int = Field(..., ge=1, le=1000)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    # 这里的正则表达式用于简单的邮箱格式校验
    # 其中，+ 表示前面的字符可以出现一次或多次，
    # \. 表示邮箱格式中的点号，在正则表达式中 . 的含义是匹配任意单个字符，换行符除外
    # {2,} 表示前面的字符至少出现两次，上不封顶


@app.post("/books2/")
def read_item2(book: Item2):
    return book



#######################             请求体的注释，样例等             #######################
class Item3(BaseModel):
    name: str = Field(title="书名", description="必填，书籍名称", example="化学必修三")

@app.post("/books3/")
def read_item3(book: Item3):
    return book




#######################             字段的自定义规则的验证             #######################
from pydantic import field_validator
class Item4(BaseModel):
    name: str = Field(...)

    @field_validator("name")
    def name_must_not_be_foo(cls, v):
        if v.lower() == "foo":
            raise ValueError("name 不能是 'foo'")
        return v

@app.post("/books4/")
def read_item4(book: Item4):
    return book


#######################             请求体某个字段需要多个值             #######################
class Item5(BaseModel):
    goods: list = Field(..., min_items=1)           # min_items 用于设置列表的最小长度，这里表示 goods 列表至少要有一个元素
    address: str = Field(default="北京市朝阳区")

@app.post("/cart/")
def read_item5(cart: Item5):
    return cart



#######################             给我举一个 list[int] 的例子            #######################

class Item6(BaseModel):
    numbers: list[int] = Field(..., min_items=1)

@app.post("/numbers/")
def read_item6(numbers: Item6):
    return numbers



# ============================                        更多 list 的用法见文件 参数的类型注解.py                        ============================ #