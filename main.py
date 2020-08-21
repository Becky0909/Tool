from fastapi import Depends, FastAPI, UploadFile, File, Form
from sqlalchemy.orm import Session
from sql_app.database import engine
import api_app.api_def as api
from sql_app import models, schemas
from starlette.requests import Request
from setting import config

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI", description="文件解析工具", version="0.1", docs_url=config.DOCS_URL,
              openapi_url=config.OPENAPI_URL, redoc_url=config.REDOC_URL)


# 华为终端报表分页
@app.post("/OperateService/operateManage/queryPageHuaWei")
def queryPageHuaWei(query: schemas.queryBase1, db: Session = Depends(api.get_db)):
    return api.pageHW(query, db)


# 小米终端报表分页
@app.post("/OperateService/operateManage/queryPageXiaoMi")
def queryPageXiaoMi(query: schemas.queryBase1, db: Session = Depends(api.get_db)):
    return api.pageXM(query, db)


# 华为终端点击报表导入/华为终端统计数据表导入
@app.post("/OperateService/operateManage/importHuaWei")
def importHuaWei(request: Request, queryType: int = Form(...),
                 subPage: int = Form(...), subSize: int = Form(...),
                 file: UploadFile = File(...), db: Session = Depends(api.get_db)):
    return api.importHW(queryType, subPage, subSize, file, db)


# 小米终端报表导入
@app.post("/OperateService/operateManage/importXiaoMi")
def importXiaoMi(request: Request, subPage: int = Form(...), subSize: int = Form(...),
                 file: UploadFile = File(...), db: Session = Depends(api.get_db)):
    return api.importXM(subPage, subSize, file, db)


@app.post("/OperateService/operateData/getHuaWeiChart")
def getHuaWeiChart(query: schemas.queryBase2, db: Session = Depends(api.get_db)):
    return api.preHW(query, db)


@app.post("/OperateService/operateData/getXiaoMiChart")
def getXiaoMiChart(query: schemas.queryBase2, db: Session = Depends(api.get_db)):
    return api.preXM(query, db)


# 华为终端点击报表模板下载/华为终端数据报表模板下载/小米终端报表模板下载
@app.get("/OperateService/operateManage/downloadTemplate/{queryType}")
def downloadTemplate(queryType, db: Session = Depends(api.get_db)):
    return api.exModel(queryType, db)


@app.post("/OperateService/operate/getNameList")
def getNameList(query: schemas.fileBase, db: Session = Depends(api.get_db)):
    return api.preNameList(query.queryType, db)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="10.10.215.80", port=8008, reload=True, debug=True)
