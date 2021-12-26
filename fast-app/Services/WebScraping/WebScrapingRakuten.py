from selenium.webdriver.common import by
from .WebScraping import WebScraping
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pandas as pd
import nlplot
import re
"""
楽天のスクレイピングクラス
"""
class WebScrapingRakuten(WebScraping):

    BASE_URL = 'https://review.rakuten.co.jp/item/1/'

    """
    コンストラクタ
    """
    def __init__(self, shohin_id: str):
        super().__init__(shohin_id=shohin_id)

    """
    ベースとなるURLを生成
    """
    def get_shohin_review_url(self):
        return WebScrapingRakuten.BASE_URL + self.shohin_id + '/'

    """
    レビューリストを返す
    """
    def get_reviews(self, page_num: int):
        browser = self.get_webdriver()

        # データフォーマットのカラム定義
        # columns = ['review_comment']
        # df = pd.DataFrame(columns=columns)
        columns = ['date', 'score', 'text', 'age', 'sex', 'url']
        df = pd.DataFrame(columns=columns)

        for i in range(page_num):
            base_url = self.get_shohin_review_url()
            url = base_url + str(i + 1) + '.1/sort6/'
            browser.get(url)
            time.sleep(2)

            reviews = browser.find_elements(by=By.CSS_SELECTOR, value="div.revRvwUserSec")

            for review in reviews:
                age_and_sex = review.find_elements(by=By.CSS_SELECTOR, value="span.revUserFaceDtlTxt span")[0].text
                age = 'なし'
                sex = 'なし'
                if age_and_sex != '':
                    [age, sex] = age_and_sex.split(' ')
                    age = int(re.sub(r"\D", "", age))

                date = review.find_element(by=By.CSS_SELECTOR, value="span.revUserEntryDate.dtreviewed").text
                score = review.find_element(by=By.CSS_SELECTOR, value="span.revUserRvwerNum.value").text
                text = review.find_element(by=By.CSS_SELECTOR, value="dd.revRvwUserEntryCmt.description").text.replace('\n','')
                se = pd.Series([date, score, text, age, sex, url], columns)
                df = df.append(se, columns)
        browser.quit()
        return df