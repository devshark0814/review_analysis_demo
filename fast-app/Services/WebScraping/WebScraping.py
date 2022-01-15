from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import pandas as pd
import nlplot

class WebScraping:
    """
    Webスクレイピングの親クラス
    """
    def __init__(self, shohin_id: str):
        """
        コンストラクタ
        """
        self.shohin_id = shohin_id

    def get_webdriver(self):
        """
        ブラウザを返す
        """
        options=webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options
        )
        return browser