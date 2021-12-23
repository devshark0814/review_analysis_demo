from selenium.webdriver.common import by
from WebScraping import WebScraping
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
        columns = ['date', 'score', 'text', 'age', 'sex']
        df = pd.DataFrame(columns=columns)

        for i in range(page_num):
            base_url = self.get_shohin_review_url()
            browser.get(base_url + str(i + 1) + '.1/sort6/')

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
                se = pd.Series([date, score, text, age, sex], columns)
                df = df.append(se, columns)

            # for j in range(1,16):
            #     val = f'//*[@id="revRvwSec"]/div[1]/div/div[2]/div[{j}]/div[2]/div[2]/div/dl/dd[1]'
            #     elem = browser.find_element(by=By.XPATH, value=val)
            #     review_comment = elem.text.replace('\n','')
            #     se = pd.Series([review_comment], columns)
            #     df = df.append(se, columns)
            time.sleep(2)
        browser.quit()
        return df