#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def execSearch(browser: webdriver, img_name: str):
    """
    Googleで検索する
    :param browser: webdriver
    """
    # Googleにアクセス
    browser.get('https://www.google.co.jp/')
    WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)

    # キーワードの入力
    search_box = browser.find_element_by_name("q")
    search_box.send_keys('hello selenium')

    # 検索実行
    search_box.submit()
    WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)

    # スクリーンショット
    browser.save_screenshot(img_name + '.png')

if __name__ == '__main__':
    # try:
    #     # UA を設定
    #     capabilities = webdriver.common.desired_capabilities.DesiredCapabilities.CHROME.copy()
    #     capabilities['javascriptEnabled'] = True

    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 4.0.3; SC-02C Build/IML74K) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.58 Mobile Safari/537.31"')

    #     # HEADLESSブラウザに接続
    #     browser = webdriver.Remote(
    #         command_executor='http://selenium-hub:4444/wd/hub',
    #         desired_capabilities=DesiredCapabilities.CHROME,
    #         options=options
    #     )

    #     browser2 = webdriver.Remote(
    #         command_executor='http://selenium-hub:4444/wd/hub',
    #         desired_capabilities=DesiredCapabilities.FIREFOX
    #     )

    #     # FBで実行
    #     execSearch(browser,  img_name='chrome')
    #     execSearch(browser2, img_name='firefox')

    #     browser.close()
    #     browser2.close()

    # finally:
    #     # 終了
    #     pass
    from selenium import webdriver
    #element指定に使用
    from selenium.webdriver.common.by import By
    #処理待ち時間の指示に使用
    import time

    import pandas as pd
    import nlplot

    options=webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    #ブラウザの立ち上げ
    # browser=webdriver.Chrome('chromedriver',options=options)


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