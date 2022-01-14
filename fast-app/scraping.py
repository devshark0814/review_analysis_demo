import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('./output.csv', index_col=0, encoding="SHIFT-JIS")
    print(df['text'])
    df["re_text"] = df['text'].str.replace("\(.+?\)|\（.+?\）|\d|[…★←！●...？?。、,☆○�👍]+","",regex=True)
    print(df['re_text'])