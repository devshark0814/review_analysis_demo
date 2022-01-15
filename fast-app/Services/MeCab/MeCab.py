import MeCab

def mecab_text(text: str):
    """
    形態素解析
    """

    #MeCabのインスタンスを作成（辞書はmecab-ipadic-neologdを使用）
    mecab = MeCab.Tagger('-Ochasen -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

    #形態素解析
    node = mecab.parseToNode(text)

    #形態素解析した結果を格納するリスト
    #{'表層系': '健康', '品詞': '名詞', '基本形': '健康'}のリスト
    dic = []

    while node:
        word = node.surface

        #品詞情報
        #品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        wclass = node.feature.split(',')
        if wclass[0] != u'BOS/EOS':
            if wclass[6] == None:
                dic.append(dict(表層系=word, 品詞=wclass[0], 基本形=""))
            else:
                dic.append(dict(表層系=word, 品詞=wclass[0], 基本形=wclass[6]))
        node = node.next
    return dic