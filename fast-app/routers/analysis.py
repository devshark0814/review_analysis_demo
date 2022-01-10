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

    key_arr = []
    val_arr = []

    for word_count in word_count_arr:
        key_arr.append(word_count[0])
        val_arr.append(word_count[1])

    print(word_count_arr)

    datas = {}
    datas['key_arr'] = key_arr[:50]
    datas['val_arr'] = val_arr[:50]

    return {"message": "分析完了", "datas" : datas}

@router.post("/get_rakuten_analysis_word_cloud")
async def get_rakuten_analysis_word_cloud():
    df = pd.read_csv('./output.csv', index_col=0, encoding="SHIFT-JIS")
    df['words'] = df['text'].apply(mecab_text)
    word_arr = list(itertools.chain.from_iterable(df['words']))

    c = collections.Counter(word_arr)
    word_count_arr = c.most_common()

    key_arr = []
    val_arr = []

    for word_count in word_count_arr:
        key_arr.append(word_count[0])
        val_arr.append(word_count[1])

    print(word_count_arr)

    datas = {}
    datas['key_arr'] = key_arr[:50]
    datas['val_arr'] = val_arr[:50]

    return {"message": "分析完了", "datas" : datas}