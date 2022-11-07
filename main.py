import uvicorn
from fastapi import FastAPI
from settings.dbconfig import engine
from apis.models import Base
from apis.views import *


app = FastAPI()
Base.metadata.create_all(engine)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
        access_log=False
    )
