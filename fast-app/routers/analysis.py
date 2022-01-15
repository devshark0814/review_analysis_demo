import sys
sys.path.append('../')
from fastapi import APIRouter
import pandas as pd
from Services.MeCab.MeCab import mecab_text
from Services.Analysis.Analysis import Analysis
import itertools

router = APIRouter()

@router.get("/")
async def index():
    """
    index
    """
    return {"message": "analysis.index()"}

@router.get("/get_cleansing_reviews")
async def get_cleansing_reviews():
    """
    データクレンジングしたレビュー結果を返す
    """
    df = Analysis.read_csv_data()
    json = df.to_dict(orient='index')
    value_list = json.values()
    value_list = list(value_list)

    return value_list

@router.get("/get_reviews_word_count")
async def get_reviews_word_count():
    """
    楽天のレビューを形態素解析して、品詞ごとに出現回数をセットして返す
    """
    df = Analysis.read_csv_data()
    # レビュー毎に二次元配列に形態素解析結果が入っている
    two_dic = df['remake_text'].apply(mecab_text)
    # 集計のために一次元配列に
    one_dic = list(itertools.chain.from_iterable(two_dic))

    result = {}     # 集計結果格納用
    datas  = {}     # 画面に返すオブジェクト

    # 名詞の集計
    result = Analysis.set_word_count(type=1, one_dic=one_dic)
    datas['meishi_y_arr'] = result['words'][:15]
    datas['meishi_x_arr'] = result['counts'][:15]

    # 動詞の集計
    result = Analysis.set_word_count(type=2, one_dic=one_dic)
    datas['doushi_y_arr'] = result['words'][:15]
    datas['doushi_x_arr'] = result['counts'][:15]

    # 形容詞の集計
    result = Analysis.set_word_count(type=3, one_dic=one_dic)
    datas['keiyoushi_y_arr'] = result['words'][:15]
    datas['keiyoushi_x_arr'] = result['counts'][:15]

    return {"message": "分析完了", "datas" : datas}

@router.get("/get_word_cloud")
async def get_word_cloud():
    """
    ワードクラウド用のデータを集計して返す
    """
    df = Analysis.read_csv_data()
    # レビュー毎に二次元配列に形態素解析結果が入っている
    two_dic = df['remake_text'].apply(mecab_text)
    # 集計のために一次元配列に
    one_dic = list(itertools.chain.from_iterable(two_dic))

    result = {}     # 集計結果格納用

    # 名詞の集計
    result = Analysis.set_word_count(type=1, one_dic=one_dic)

    datas = list(zip(result['words'], result['counts']))
    # c = collections.Counter(one_dic)
    # word_count_arr = c.most_common()

    return {"message": "分析完了", "datas" : datas}