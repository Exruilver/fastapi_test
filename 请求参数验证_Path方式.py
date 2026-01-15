from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items1/{item_id}")
def read_item1(item_id: int = Path(..., ge=1, le=100, title="The ID of the item to get", description="必须在 1 到 100 之间的整数")):
    """
        通过 Path 函数对路径参数进行校验
        ge: 大于等于
        le: 小于等于
        title: 参数标题
        description: 参数描述
    """
    return {"item_id": item_id}



# 下面这种写法是错误的，Path 函数的第一个参数不能是默认值
# @app.get("/items2/{item_id}")
# def read_item2(item_id: str = Path(123)):
#     return {"item_id": item_id}



# 可以使用 Path 函数对路径参数进行字符串长度校验
@app.get("/items3/{item_id}")
def read_item3(item_id: str = Path(...,min_length=3,max_length=12)):
    return {"item_id": item_id}




# 数值大小进行校验
@app.get("/items4/{item_id}")
def read_item(item_id: float = Path(...,gt=3,lt=10)):
    return {"item_id": item_id}



# 正则表达式校验
@app.get("/items5/{item_id}")
def read_item5(item_id: str = Path(...,regex="^[a-zA-Z][a-zA-Z0-9_]{3,15}$"
                                   ,description="必须以字母开头，长度在4-16之间，只能包含字母、数字")):
    """
        这里的正则表达式相当于 ^[a-zA-Z]\w{3,15}$
        \w 表示任意的字母、数字、下划线
        必须以字母开头，长度在4-16之间，只能包含字母、数字、下划线或减号
    """
    return {"item_id": item_id}



# 正则表达式校验2    下面这个正则表达式是在匹配 color 和 colour 两种拼写方式
@app.get("/items6/{item_id}")
def read_item6(item_id: str = Path(...,regex="^colou?r$"
                                   ,description="匹配 color 和 colour 两种拼写方式")):
    """
        ? 表示前面的字母 u 出现 0 次或 1 次也就是可有可无
        r 是固定匹配的字母
    """
    return {"item_id": item_id}




# 多个路径参数校验
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(
    user_id: int = Path(...,gt=0,description="用户 ID 必须大于 0"),
    item_id: str = Path(...,min_length=3, max_length=12, description="物品 ID 长度必须在 3 到 12 之间")
):
    return {"user_id": user_id, "item_id": item_id}



# 当路径参数是一个枚举类型时，可以使用 Enum 类进行校验
# 应用场景：比如模型名称只能是固定的几种，多选一
from enum import Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName = Path(...,description="模型名称只能是 alexnet、resnet、lenet 之一")):
    """
        这里的路径参数 model_name 是一个枚举类型
        只能是枚举类 ModelName 中定义的值之一
    """
    return {"model_name": model_name}   




