"""
    在 FastAPI 中，可以使用类型注解来指定路径参数和查询参数的数据类型。
    来完成数据类型的校验
"""
# 这是一条注释

from typing import Union,List,Optional
from fastapi import FastAPI


app = FastAPI()
#99999


# 当需要的参数是若干种数据类型中的一种时，可以使用 | 符号来表示多种类型
@app.get("/mix0/{item_id}")
def read_item0(item_id: int | str):
    """ 路径参数 item_id 可以是整数类型也可以是字符串类型 """
    return {"item_id": item_id}




@app.get("/mix1/{item_id}")
def read_item1(item_id: Union[int, bool]):

    """ 
        路径参数 item_id 可以是整数类型也可以是字符串类型 
        这种写法需要导入 typing 模块中的 Union 类型
    """
    return {"item_id": item_id}

"""
    注意：在 python 中字符串类型一般支持 int 类型转换，所以如果传入的路径参数是 "123" 这种字符串，
         FastAPI 会自动将其转换为 int 类型，而不会报错。
         如果希望路径参数严格按照指定的数据类型进行校验，可以在函数体内添加额外的校验逻辑。

"""




# 路径参数不可以设置默认值
@app.get("/mix2/{item_id}")
def read_item2(item_id: Union[int, str] = 42):
    """ 这种写法会报错 """
    return {"item_id": item_id}




# 查询参数中可以使用默认值，包括 Union 类型
@app.get("/mix3/")
def read_item2(item_id: Union[int, str] = 42):
    return {"item_id": item_id}



# 对于参数传还是不传，可以使用 None 来表示参数可选
@app.get("/mix4/")
def read_item4(item_id: int = None):
    # 也可以写作 item_id: Union[int, None] = None 或者 item_id: int | None = None
    return {"item_id": item_id}



# 当单个请求参数需要传入很多个值的时候，可以使用 list 作为类型注解
@app.get("/mix5/")
def read_item5(q: list):
    # 这里单个参数 q 的类型是 list，可以传入多个值，比如 ?q=foo&q=bar
    # 但是这些值的默认类型是字符串
    return {"q": q}
# 为什么上述这种写法是请求体参数呢？
# 因为 list 是一个复杂数据类型，不能直接作为查询参数传入
# FastAPI 会将其作为请求体参数进行处理
# 所以使用 list, dict 等复杂数据类型作为参数类型注解时，建议使用 POST 请求方法


# 如果希望传入的多个值是指定类型的，可以使用 List 类型注解
@app.get("/mix6/")
def read_item6(q: List[int]):
    # 这里单个参数 q 的类型是 List[int]，可以传入多个整数值，比如 ?q=1&q=2&q=3
    return {"q": q}



# 注意上面这种写法的请求方法不应该是 GET，而应该是 POST，因为传入的参数是请求体参数
@app.post("/mix7/")
def read_item7(q: List[int]):
    # 这里单个参数 q 的类型是 List[int]，可以传入多个整数值，比如在请求体中传入 [1,2,3]
    return {"q": q}


@app.post("/mix8/")
def read_item7(q: List):
    return {"q": q}