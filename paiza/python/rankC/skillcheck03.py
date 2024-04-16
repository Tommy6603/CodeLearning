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

入力される値
入力は以下のフォーマットで与えられます。

N
W_1
W_2
...
W_N

1 行目には検索ワードの数を表す整数 N が与えられます。
続く N 行では検索ワード W_i が与えられます。
続く N 行のうちの i 行目 (1 ≦ i ≦ N) には、検索ワード W_i が与えられます。検索ワード W_i は小文字のアルファベット a ~ z のみからなる文字列です。
入力は合計 N + 1 行であり、 最終行の末尾に改行が 1 つ入ります。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。

期待する出力
検索ワードを N 個入力した後の検索履歴を出力してください。
出力の最後に改行を入れ、余計な文字、空行を含んではいけません。

条件
すべてのテストケースにおいて、以下の条件をみたします。

1 ≦ N ≦ 100
各 W_i (1 ≦ i ≦ N) に対して、W_iの文字数が20を超えない。
"""
import sys
from collections import deque

def update_search_history(history, term):
    if term in history:
        history.remove(term)
    history.appendleft(term)

def main():
    input = sys.stdin.read #改行含めて入力可能。ctrl+Dでescape
    data = input().split() #スペースタブ改行を区切り文字としてリストに分ける
    
    N = int(data[0])
    search_terms = data[1:] #２つめの要素以降のリストを作成。スライス記法。
    
    history = deque() #deque型にする。両端から要素の追加削除ができる
    
    for term in search_terms:
        update_search_history(history, term)
    
    for term in history: #historyを順番に表示する
        print(term)

if __name__ == '__main__':
    main()