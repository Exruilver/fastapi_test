from fastapi import FastAPI




# 1.在终端启动服务
# uvicorn 文件名:对象名 --reload

# 2. 在终端使用 fastapi 框架提供的调试功能启动
# fastapi dev 完整文件名

# 3. 在编辑器中运行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("aaa:app", host="127.0.0.1", port=8000)



















app = FastAPI()


# 这里括号中的内容表示资源路径也叫做路由
@app.get("/fuck/666")
def read_root():
    return {"Hello": "Wor付出考试iu对方算的奶粉old"}   


@app.get("/items/{id}")
# 这行代码的表示浏览器的 url 地址中的 id 是一个参数，我们在访问这个资源的时候，会将 id 作为参数传入下面定义的函数中
def read_item(id: int):       
    return {"item_iffffd": id} 


# 该资源路径需要传入两个不同查询参数
@app.get("/query")
def page_limit(p5ge, limit):        # 函数中的两个是参数名，也是 url 中查询参数的 key
    return {
            "page":p5ge,
            "limit": limit
            }

# 下面这种情况是查询参数同时设置了数据类型和默认值
@app.get("/query2")
def page_limit2(page: int, limit = None):      # 注意默认值参数只能放在最右边
    if limit:
        return {
            "page": page,
            "limit": limit
        }
    else:
        return {
            "page": page
        }


# 下面这种情况是 url 同时需要路径参数和查询参数
@app.get("/query3/{page}")
def page_limit3(page: int, limit: int = None):

    # 如果 limit 为 None，则只返回路径参数 page
    if limit is None:
        return {
            "这是路径参数 page": page
        }
    # 如果 limit 不为 None，则返回路径参数 page 和查询参数 limit
    else:
        return {
            "这是路径参数 page":page,
            "这是查询参数limit": limit
        }


"""
    注意：路径参数在装饰器的括号里面要用花括号包裹，而查询参数不需要，而且路径
    参数必须出现在 url 中，而查询参数可以省略不写
"""




# 路径参数不可以设置默认值
@app.get("/mix3/{item_id}")
def read_item3(item_id: int = 42):
    """ 这种写法会报错 """
    return {"item_id": item_id}





# 路径参数不可以设置默认值
# 对于参数传还是不传，可以使用 None 来表示参数可选
@app.get("/mix4/")
def read_item4(item_id: int = None):
    # 也可以写作 item_id: Union[int, None] = None 或者 item_id: int | None = None
    return {"item_id": item_id}



