"""
神経衰弱と呼ばれるトランプゲームのシミュレーションをしましょう。
今回は数字が書かれたトランプのみを考え、ジョーカーは考えません。

まず、トランプを縦 H 枚、横 W 枚の長方形の形に並べた状態でスタートします。
H × W 枚のトランプには 1 〜 13 の数字のうちどれか1つが書かれています。
また、同じ数字が書かれたトランプが複数あります。

プレイヤーが N 人おり、それぞれ 1 〜 N で番号付けられています。
ゲームが始まると、1番の人から、このような手順でプレイしていきます。

・並べられたトランプから2枚のトランプを選び、めくります。
・めくった2枚のトランプに異なる数字が書かれていれば、次のプレイヤーの手番となります。同じ数字であれば、次の操作をおこないます。
・まず、2枚のトランプはめくったプレーヤーのものとなり、取り除かれます。
・トランプがすべて取り除かれた場合、ゲームは終了となります。
・トランプが残っている場合、同じプレーヤーがまた最初の手順に戻り、トランプをめくります。

ここで、N 番のプレイヤーの次のプレイヤーは 1 番のプレイヤーであるとします。

ゲームの初期状態におけるトランプの配置と、ゲームが終わるまでに捲られたトランプに関する時系列順の記録が与えられます。
その記録を用いて、各プレイヤーが取り除いたトランプの枚数を求めてください。

入力される値
入力は以下のフォーマットで与えられます。

H W N
t_{1,1} t_{1,2} ... t_{1,W}
t_{2,1} t_{2,2} ... t_{2,W}
...
t_{H,1} t_{H,2} ... t_{H,W}
L
a_1 b_1 A_1 B_1
a_2 b_2 A_2 B_2
...
a_L b_L A_L B_L

1行目には3つの整数 H, W, Nが入力されます。
H と W はそれぞれ並べられたトランプの縦方向の枚数と横方向の枚数で、N はプレイヤーの数を表します。

続く H 行には、配置されたトランプに書かれた数字が入力されます。
t_{i,j} は i 行 j 列に置かれたトランプに書かれた数字を表します。

次の行には、記録の長さ L が与えられます。

続く L 行には、捲られたトランプの記録が時系列順で与えられます。
これは、a_i 行 b_i 列のトランプと A_i 行 B_i 列のトランプが捲られたことを表します。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。

期待する出力
i 行目には i 番目のプレイヤーが取り除いたトランプの枚数を出力してください。
各行の最後は改行し、余計な文字、空行を含んではいけません。

すべてのテストケースにおいて、以下の条件をみたします。

・1 ≦ H, W ≦ 13
・H × W は52以下の2の倍数
・2 ≦ N ≦ 10
・t_{i,j} は 1, ... ,13 のいずれか
・並べられたトランプの中に、同じ数字が書かれたトランプは2枚または4枚ある
・1 ≦ L ≦ 200
・1 ≦ a_i, A_i ≦ H
・1 ≦ b_i, B_i ≦ W
・a_i 行 b_i 列および A_i 行 B_i 列のトランプは取り除かれていない
・(a_i, b_i) ≠ (A_i, B_i)

入力例1
2 3 2
1 2 3
2 1 3
5
1 1 2 1
1 1 1 2
1 1 2 2
1 3 2 3
1 2 2 1

出力例1
6
0
"""

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # トランプの配置サイズとプレイヤー数を読み込む
    H = int(data[0])
    W = int(data[1])
    N = int(data[2])
    
    # トランプの配置を読み込む
    idx = 3
    cards = []
    for _ in range(H):
        cards.append([int(data[idx + j]) for j in range(W)])
        idx += W
        
    # ゲーム記録の長さ
    L = int(data[idx])
    idx += 1
    
    # ゲーム記録を読み込む
    moves = []
    for _ in range(L):
        a = int(data[idx]) - 1
        b = int(data[idx + 1]) - 1
        A = int(data[idx + 2]) - 1
        B = int(data[idx + 3]) - 1
        moves.append((a, b, A, B))
        idx += 4
    
    # プレイヤーごとに取ったカードの数を記録する配列
    scores = [0] * N
    
    # カードが取られたかどうかの状態を管理する
    removed = [[False] * W for _ in range(H)]
    
    # 現在のプレイヤー番号（0-indexed）
    current_player = 0
    
    for a, b, A, B in moves:
        if not removed[a][b] and not removed[A][B]:
            # カードをめくる
            card1 = cards[a][b]
            card2 = cards[A][B]
            
            if card1 == card2:
                # カードがマッチした場合
                scores[current_player] += 2  # このプレイヤーがカードを2枚取る
                removed[a][b] = True
                removed[A][B] = True
                # 同じプレイヤーのターンが続く
            else:
                # マッチしなかった場合、次のプレイヤーへ
                current_player = (current_player + 1) % N
    
    # 結果を出力
    print(scores)
    for score in scores:
        print(score)

if __name__ == "__main__":
    main()
