import sys
sys.path.append('../')
from fastapi import APIRouter
import pandas as pd
from Services.MeCab.MeCab import mecab_text
import itertools
import collections

router = APIRouter()

@router.post("/")
async def index():
    return {"message": "analysis.index()"}

@router.post("/get_rakuten_analysis")
async def get_rakuten_analysis():
    df = pd.read_csv('./output.csv', index_col=0, encoding="SHIFT-JIS")
    df['words'] = df['text'].apply(mecab_text)
    word_arr = list(itertools.chain.from_iterable(df['words']))

    c = collections.Counter(word_arr)
    word_count_arr = c.most_common()

    print(df['words'])
    print(word_arr)
    print(word_count_arr)

    return {"message": "分析完了！", "datas" : word_count_arr}