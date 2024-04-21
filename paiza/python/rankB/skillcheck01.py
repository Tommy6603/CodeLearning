"""
あなたは友達たちと N 人でしりとりを行うことにしました。
1 人目、 2 人目、...、 N 人目、 1 人目、2 人目、... という順序で発言をします。

ここで、それぞれの人は、次に挙げる 4 つのしりとりのルールを守って発言をする必要があります。

1. 発言は、単語リストにある K 個の単語のうちのいずれかの単語でなければならない。
2. 最初の人以外の発言の頭文字は、直前の人の発言の最後の文字と一緒でなければならない。
3. 今までに発言された単語を発言してはならない。
4. z で終わる単語を発言してはならない。

ここで、発言の途中で上のルールを破った場合、ルールを破った人はしりとりから外れます。
そして、その人を抜いて引き続きしりとりを続けていきます。このとき、後続の人は、ルール 2 を守る必要はありません。

N 人がしりとりを行ったログが M 行分与えられます。
このとき、M 回の発言が終わった後、しりとりから脱落せずに残っている人のリストを表示するプログラムを書いてください。

入力される値
入力は以下のフォーマットで与えられます。

N K M
d_1
d_2
...
d_K
s_1
s_2
...
s_M

・1 行目にしりとりをする人数を表す整数 N、単語リストに乗っている単語の数を表す整数 K、しりとりで行われた発言の数を表す整数 M がこの順にスペース区切りで与えられます。
・続く K 行のうちの i 行目 (1 ≦ i ≦ K) には、単語リストに乗っている i 番目の単語を表す文字列 d_i が与えられます。
・続く M 行のうちの j 行目 (1 ≦ j ≦ M) には、しりとりで行われた j 番目の発言を表す文字列 s_j が与えられます。
・入力は合計で K + M + 1 行となり、入力値最終行の末尾に改行が 1 つ入ります。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
最終的にしりとりから脱落せずに残っている人の番号を以下の形式で出力してください。

N'
a_1
a_2
...
a_N'

期待する出力は N' + 1 行からなります。
1 行目には、最終的にしりとりから脱落せずに残っている人の人数を表す整数 N' を出力してください。
続く N' 行のうち、i 行目 (1 ≦ i ≦ N') には、最終的にしりとりから脱落せずに残っている人の番号のうち、小さい方から i 番目のものを出力してください。
N' + 1 行目の出力の最後に改行を入れ、余計な文字、空行を含んではいけません。

条件
すべてのテストケースにおいて、以下の条件をみたします。

1 ≦ N ≦ 10
1 ≦ K ≦ 1,000
1 ≦ M ≦ 1,000

各 i, i' (1 ≦ i, i' ≦ K) について
1 ≦ (d_i の長さ) ≦ 10
i ≠ i' なら d_i ≠ d_i'

各 j (1 ≦ j ≦ M) について
1 ≦ (s_j の長さ) ≦ 10

少なくとも 1 人はしりとりから脱落しないことが保証されている

入力例
3 6 7
a 
aloha
app
az
paiza
warp
app 
paiza
a
aloha
az
warp
paiza

出力例
1
3

入力例2
4 4 4
abacus
banana
candy
yankee
banana
candies
candies
yankee

出力例2
2
1
4
"""


import sys
input = sys.stdin.read
data = input().split()

# 最初の行の解析 range(0:3)
index = 0
N = int(data[index]) # 人数
K = int(data[index + 1]) # 単語数
M = int(data[index + 2]) # 行数
index += 3

# 単語リストの読み込み range(3 : 3 + K)
valid_words = set() #集合作成: 重複要素なし&順序なし→重複要素を自動で消してくれる
for i in range(K):
    valid_words.add(data[index + i]) #要素の追加 *追加方法が異なる
index += K

# しりとりログの読み込み range(3 + K : 3 + K + M)
shiritori_log = [] #リスト：重複も残す必要がある
for j in range(M):
    shiritori_log.append(data[index + j]) #要素の追加
index += M

# ゲームの状態変数
remaining_players = set(range(1, N + 1))
#print(remaining_players)
used_words = set()
last_speaker = None
last_char = None

# ゲームのシミュレーション
for i, word in enumerate(shiritori_log): # 与えられた行列のindexと要素をセットで返す
    if len(remaining_players) == 0: # 残りプレイヤーが0人で終了　起こらない
        break

    current_player = (i % N) + 1
    if current_player not in remaining_players:
        continue #次のループに移行

    if word not in valid_words or word in used_words or (last_char is not None and word[0] != last_char) or word[-1] == 'z':# NGワード
        remaining_players.remove(current_player)
        last_char = None  # このプレイヤーが脱落したので次のプレイヤーには最後の文字の制約がなくなる
    else:
        used_words.add(word)
        last_char = word[-1]

    last_speaker = current_player

# 結果の出力
print(len(remaining_players))
for player in sorted(remaining_players):
    print(player)
    
