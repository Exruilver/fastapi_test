from fastapi import FastAPI, HTTPException

app = FastAPI()



#######################             基本用法             #######################

# 当前需求是按照日期查询新闻，如果传入日期非法，发挥错误信息

@app.get("/news/{date}")
def get_news1(date: int):
    if date not in range(1,32):
        raise HTTPException(status_code=404, detail="你所输入的信息不正确")
    
    return {"content": f"当前你查询的是{date}号的新闻"}
    