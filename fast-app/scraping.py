#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pandas as pd
import nlplot

"""
WEBスクレイピング（楽天）を実行するクラス
"""
class WebScraping:
    """
    コンストラクタ
    """
    def __init__(self, shohin_id: str):
        self.shohin_id = shohin_id
        print(self.shohin_id)

class WebScrapingRakuten(WebScraping):
    """
    コンストラクタ
    """
    def __init__(self, shohin_id: str):
        super().__init__(shohin_id)

    def scraping():
        options=webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options
        )

        # レビュー画面のURL
        SHOHIN_ID = '212142_10126692'
        URL = 'https://review.rakuten.co.jp/item/1/' + SHOHIN_ID + '/'

        # 繰り返し数（レビュー画面の3ページ分）
        times = 2

        # データフォーマットのカラム定義
        columns = ['review_comment']
        df = pd.DataFrame(columns=columns)

        reviews = []
        for i in range(1, times):
            browser.get(URL + str(i + 1) + '.1/')
            # エレメントの指定
            for j in range(1,16):
                val = f'//*[@id="revRvwSec"]/div[1]/div/div[2]/div[{j}]/div[2]/div[2]/div/dl/dd[1]'
                elem = browser.find_element(by=By.XPATH, value=val)
                review_comment = elem.text.replace('\n','')
                se = pd.Series([review_comment], columns)
                df = df.append(se, columns)
            time.sleep(2)
            # ブラウザーのシャットダウン 
            browser.quit()
        print(df)
        print("main")

if __name__ == '__main__':
    s = WebScrapingRakuten('212142_10126692')