from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/html1", response_class=HTMLResponse)
def get_html1():
    html_content = """
    <html>
        <head>
            <title>HTML Response Example</title>
        </head>
        <body>
            <h1>This is an HTML Response</h1>
            <h2>这是使用 FastAPI 返回的 HTML 页面  这是一个小标题</h2>
            <p>Hello, welcome to the FastAPI HTML response example!</p>
        </body>
    </html>
    """
    # 这里可以通过 status_code 参数自定义响应状态码
    return HTMLResponse(content=html_content, status_code=201)



# 最后 return 的内容会作为响应体返回给客户端，也可以不使用 HTMLResponse
# 直接 return html 内容，FastAPI 会自动识别并返回 HTML 页面


# 路由参数一定要指定 response_class=HTMLResponse
@app.get("/html2", response_class=HTMLResponse)
def get_html2():
    return "<h1> 这是一级标题 </h1> <h2> 这是二级标题" \
    " </h2> <p> 这是一个段落 </p>"
