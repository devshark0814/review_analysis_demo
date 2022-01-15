from fastapi import FastAPI
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware
from routers import scraping, analysis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(scraping.router, prefix="/api/scraping", tags=["scraping"])
app.include_router(analysis.router, prefix="/api/analysis/rakuten", tags=["analysis/rakuten"])