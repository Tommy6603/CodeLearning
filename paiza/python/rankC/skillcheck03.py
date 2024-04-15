"""
https://paiza.jp/works/mondai/c_rank_skillcheck_archive/search_history?language_uid=python3 
あなたが利用しているブラウザでは検索ワードの履歴を見ることができません。あなたは検索ワードの履歴を見られないのは不便だと思ったので、検索ワードの履歴を見る機能を自分でつくることにしました。

検索ワードの履歴とは次のようにつくられます。

検索ワード W が以前に入力されたことがある場合：
履歴中の W を削除する。
履歴の先頭に W を追加する。
検索ワード W が以前に入力されたことがない場合：
履歴の先頭に W を追加する。

検索ワード W が N 個与えられるので、N 個の検索ワードが与えられた後の履歴を表示するプログラムを書いてください。
"""

from collections import deque

def manage_search_history(search_terms):
    history = deque()  # 両端から要素を追加・削除できる。queやstackの実装に適している
    for term in search_terms:
        if term in history:
            history.remove(term)  # 履歴に存在する場合は削除
        history.appendleft(term)  # 履歴の最前面に追加(全てのwordに適用)
    return list(history)

# 検索ワードのリスト（入力）
search_terms = ["apple", "banana", "apple", "orange", "mango", "banana"]

# 検索履歴を更新し、結果を表示
updated_history = manage_search_history(search_terms)
print("Updated search history:", updated_history)