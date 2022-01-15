import re
import sys
sys.path.append('../')
from fastapi import APIRouter
from schemas.textMining import SimpleMecabResultModel
from Services.MeCab.MeCab import mecab_text
import itertools

router = APIRouter()

@router.post("/")
async def index():
    """
    index
    """
    return {"message": "textMining.index()"}

@router.post("/get_simple_mecab_result")
async def get_simple_mecab_result(req: SimpleMecabResultModel):
    """
    一文を引数でもらい、単純なmecabの解析結果を返す
    """
    return mecab_text(req.text)