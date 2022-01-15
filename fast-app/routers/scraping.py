import sys
sys.path.append('../')
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.scraping import ScrapingSettingRakuten, ScrapingResult
from Services.WebScraping.WebScrapingRakuten import WebScrapingRakuten

router = APIRouter()

@router.post("/")
async def index():
    """
    index
    """
    return {"message": "scraping.index()"}

@router.post("/getReviews")
async def getReviews(req: ScrapingSettingRakuten):
    """
    商品IDを元に楽天のレビューページをスクレイピング<br>
    結果をCSVに保存
    """
    shohin_id = req.shohin_id
    repeat = req.repeat

    # スクレイピング実行
    sc = WebScrapingRakuten(shohin_id=shohin_id)
    url = sc.get_shohin_review_url()
    ScrapingResult.page_url = url

    # スクレイピング結果をCSVに保存
    df = sc.get_reviews(repeat)
    json = df.to_dict(orient='index')
    df.to_csv("./output.csv", encoding='shift_jis')

    value_list = json.values()
    value_list = list(value_list)

    return {"message": "スクレイピング完了!", "datas": value_list}