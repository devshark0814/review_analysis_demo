import re
import sys
sys.path.append('../')
from fastapi import APIRouter
from schemas.textMining import SimpleMecabResultModel
from Services.MeCab.MeCab import simple_mecab_text
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
    # レビュー毎に二次元配列に形態素解析結果が入っている
    # two_dic = req.text.apply(mecab_text)
    two_dic = simple_mecab_text(req.text)
    # 集計のために一次元配列に
    # one_dic = list(itertools.chain.from_iterable(two_dic))

    return two_dic