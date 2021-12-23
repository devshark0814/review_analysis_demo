from WebScrapingRakuten import WebScrapingRakuten

if __name__ == '__main__':
    s = WebScrapingRakuten('212142_10126692')
    url = s.get_shohin_review_url()
    print(url)
    df = s.get_reviews(3)
    df.to_csv("./output.csv", encoding='shift_jis')
    print(df)