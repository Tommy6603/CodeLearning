"""
マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ... S_H が与えられるので、
隣接する上下左右のマスが全て '#' であるマスの y , x 座標 を答えてください。

ただし、左端のマスの場合は「右のマスが '#' 」であれば、右端のマスの場合は「左のマスが '#' 」であれば隣接する左右のマスが全て '#' であるものとします。
また、上端のマスの場合は「下のマスが '#' 」であれば、下端のマスの場合は「上のマスが '#' 」であれば隣接する上下のマスが全て "#" であるものとします。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

入力される値
H W     
S_0     
...     
S_(H-1)

・ 1 行目には盤面の行数を表す整数 H , 盤面の列数を表す整数 W が与えられます。
・ 続く H 行のうち i 行目 (0 ≦ i < H) には、盤面の i 行目の文字をまとめた文字列 S_i が与えられ、 S_i の j 文字目は、盤面の i 行目の j 列目に書かれている文字を表します。(0 ≦ j < W)
入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
N (1 ≦ N ≦ H×W) 行の出力
・ 条件を満たすマスの y , x 座標を出力してください。
・ 左上 (y = 0, x = 0) のマスから順に、x 座標 , y 座標の順で増加するように出力してください。詳しくは入出力例を参考にしてください。

y_1 x_1
...
y_N x_N

条件
すべてのテストケースにおいて、以下の条件をみたします。
・ 1 ≦ H, W ≦ 20
・ S は W 文字の文字列
・ S の各文字は '.' または '#'
・ 条件を満たすマスが少なくとも 1 つ以上存在します

入力例1
3 3
##.
###
...

出力例1
0 0
0 2

入力例2
10 10
##########
..........
##########
##########
..........
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
..........

出力例2
6 0
6 2
6 4
6 6
6 8
7 1
7 3
7 5
7 7
7 9
"""

def find_surrounded_cells():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    H = int(data[0])
    W = int(data[1])
    grid = data[2:]
    
    surrounded_cells = []
    
    # Check each cell in the grid
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                # Check the four possible neighbors
                up = grid[i-1][j] if i > 0 else '#'
                down = grid[i+1][j] if i < H-1 else '#'
                left = grid[i][j-1] if j > 0 else '#'
                right = grid[i][j+1] if j < W-1 else '#'
                
                # If all adjacent cells (considering edges as always '#') are '#', we record the position
                if up == '#' and down == '#' and left == '#' and right == '#':
                    surrounded_cells.append((i, j))
    
    # Print out the results
    for cell in surrounded_cells:
        print(f'{cell[0]} {cell[1]}')

find_surrounded_cells()

