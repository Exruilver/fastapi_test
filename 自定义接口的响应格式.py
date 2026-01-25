
# 关于 BaseModel 的其他使用方法可以参考表单类型传参，请求体参数传参数


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class News(BaseModel):
    id: int
    title: str
    content: str=None   # 可以设置默认值的



#######################             基本使用             #######################

@app.get("/book1/{id}", response_model=News)
def getbook1(id):
    return{  
        "id": id,
        "title": "查理九世",
        "content": f"这是第{id}本书"
    }




# 在下面的接口中，return 是缺少返回参数的
@app.get("/book2/{id}", response_model=News, description="这里的 return 缺少返回参数 content ")
def getbook2(id):
    return{  
        "id": id,
        "title": "查理九世",
    }