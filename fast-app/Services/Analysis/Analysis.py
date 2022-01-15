from itertools import count
import pandas as pd
from collections import defaultdict

class Analysis:
    def __init__(self) -> None:
        pass

    def read_csv_data():
        """
        スクレイピングしたCSVデータを読み
        """
        df = pd.read_csv('./output.csv', index_col=0, encoding="SHIFT-JIS")
        # 正規表現で不要な文字を除外
        df["remake_text"] = df['text'].str.replace("\(.+?\)|\（.+?\）|\d|[…★←！●...？?。、,☆○�👍]+","",regex=True)
        return df

    def set_word_count(type: int, one_dic: dict):
        """[summary]
        品詞ごとの単語リストと単語出現回数のリストをセットして返す
        Args:
            type (int): 品詞のタイプ(1:名詞,2:動詞,3:形容詞)
            one_dict (dict): 形態素解析結果の一次元配列
        """
        count_dic = defaultdict(int)
        #単語の集計
        for i in one_dic:
            # 1文字だけだと集計しても分かりにくいので２文字以上を集計する
            if int(len(i["基本形"])) >= 2:
                if type == 1 and i["品詞"] == "名詞":
                        count_dic[i["基本形"]] += 1
                elif type == 2 and i["品詞"] == "動詞":
                        count_dic[i["基本形"]] += 1
                elif type == 3 and i["品詞"] == "形容詞":
                        count_dic[i["基本形"]] += 1

        #降順にソート
        sort_dic = sorted(count_dic.items(),key=lambda x : x[1],reverse=True)

        #単語と出現回数を抽出
        words  = [i[0] for i in sort_dic]
        counts = [i[1] for i in sort_dic]

        return {"words": words, "counts": counts}
