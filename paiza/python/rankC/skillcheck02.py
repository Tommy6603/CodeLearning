""""
スペースで区切られた英単語列が与えられます。
英単語列に含まれる英単語の出現回数を出現した順番に出力してください。
"""

""" example of output
input: red green blue blue green blue

red 1
green 2
blue 3
"""
from collections import OrderedDict

input_words = input("type words : ")
words_list = input_words.split()

# 単語の出現回数を記録するためのOrderedDictを作成
#https://qiita.com/apollo_program/items/165fb01b52702274936c
word_count = OrderedDict()

""""
「orderedDict」：クラスのコンストラクタの呼び出し
→OrderedDictオブジェクトを作成し、word_countに代入
・要素が追加された順序を記憶する辞書型のデータ構造
・明示的に要素の順序を保持
*dict :  要素の順序を保証しない(Python 3.7以前)
"""

# 各単語の出現回数をカウント
# word_coutのキーをforで回し回数をカウント
for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1 #新しい単語が表示された時に登録(coutを1にする)

# 出現した順番に単語とその出現回数を出力
for word, count in word_count.items():#itemメソッド：辞書内の各キーのペアをタプルとして返す
    print(f"{word}: {count}回")# f-string: 文字列を置き換えられる

"""
文字列と変数をprintで表示する方法
①コンマを使用
②+を使用*数字を文字列に変換する必要あり
③文字列フォーマット
a. formatメソッド
b. f-string
c. %を使用*古い
"""