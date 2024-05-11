"""
開始時点の x , y 座標、移動の回数 N が与えられます。
続くN行で移動の向き d1 ... dN が与えられるので、与えられた順に移動をしたときの各移動後の x , y 座標 を答えてください。
移動者ははじめ北を向いています。
なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

・ 移動をするごとに向く方角が変わること
・ 移動前に向いている方角によって同じ移動の向きでも座標の変化が違うこと
の 2 点に気をつけてください。
例えば、上の図の状態から右に移動を行った場合、下の図のような状態になります。

入力される値
X Y N       
d1      
...     
dN

・ 1 行目には、開始時点の x , y 座標を表す X , Y, 移動の回数 N が与えられます。
・ 続く N 行 (1 ≦ i ≦ N) には、盤面の i 回目の移動の向きを表す文字 d_i が与えられます。
入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
N 行での出力
・ 各移動後の x , y 座標を出力してください。

x_1 y_1
...
x_N y_N

条件
すべてのテストケースにおいて、以下の条件をみたします。
・ -100 ≦ X, Y ≦ 100
・ 1 ≦ N ≦ 100
・ d は、L, R のいずれかでそれぞれ 左・右 に １ マス進むことを表す。

入力例1
3 5 1
L

出力例1
2 5

入力例2
-18 45 6
L
L
R
R
L
R

出力例2
-19 45
-19 46
-20 46
-20 45
-21 45
-21 44

"""

def simulate_movements(x, y, N, directions):
    # Define initial conditions
    current_x, current_y = x, y
    facing = 0  # 0: North, 1: East, 2: South, 3: West
    outputs = []

    # Map for direction change: 'L' and 'R' indicate changes in the facing direction
    direction_change = {
        'L': -1,
        'R': 1
    }

    # Movement vectors for each direction North, East, South, West
    movements = [
        (0, -1),  # North: y decreases
        (1, 0),   # East: x increases
        (0, 1),   # South: y increases
        (-1, 0)   # West: x decreases
    ]

    # Process each movement direction given
    for move in directions:
        # Update facing based on direction ('L' or 'R')
        facing = (facing + direction_change[move]) % 4
        
        # Move in the direction faced
        move_vector = movements[facing]
        current_x += move_vector[0]
        current_y += move_vector[1]
        
        # Store the result after this move
        outputs.append(f"{current_x} {current_y}")

    return outputs

# Usage example:
x = -18
y = 45
N = 6
directions = ["L", "L", "R", "R", "L", "R"]

# Simulate movements and print the outputs
results = simulate_movements(x, y, N, directions)
for result in results:
    print(result)
