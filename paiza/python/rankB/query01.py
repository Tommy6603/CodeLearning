"""
paiza 君のクラスには paiza 君を含めて N + 1 人の生徒がいます。paiza 君の身長は P cm で、他の N 人の生徒の身長はそれぞれ A_1 ... A_N です。
このクラスには次のようなイベントが合計 K 回起こります。
それぞれのイベントは以下のうちのいずれかです。

・転校生がクラスに加入する
・全員で背の順に並ぶ

全員で背の順で並ぶイベントが起こるたびに、そのとき paiza 君は前から何番目に並ぶことになるかを出力してください。

入力される値
N K P
A_1
...
A_N
event_1
...
event_K


・1 行目では、paiza 君を除いたクラスの人数 N と起こるイベントの回数 K と paiza君の身長 P が与えられます。
・続く N 行では、初めにクラスにいる N 人の生徒の身長が与えられます。
・続く K 行では、起こるイベントを表す文字列が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
・全員で背の順で並ぶイベントが起こるたびに、paiza 君が前から何番目に並ぶことになるかを出力してください。
・また、出力の末尾には改行を入れてください。

条件
・1 ≦ N , K ≦ 100,000
・100 ≦ P ≦ 200
・100 ≦ A_i ≦ 200 (1 ≦ i ≦ N)
・転校生を含め、クラスの中で P cm の生徒は paiza 君のみであることが保証されている
・event_i (1 ≦ i ≦ K) は以下のいずれかの形式で与えられる。
join num
身長 num(cm) の生徒がクラスに加入したことを表す。

sorting
生徒が背の順に並ぶことを表す
この入力が与えられるたび、paiza 君が背の順で前から何番目に並ぶことになるかを出力してください。


入力例1
3 3 176
118
174
133
join 137
join 177
sorting

出力例1
5

入力例2
10 10 145
169
164
162
112
191
168
168
199
176
146
join 196
join 142
sorting
sorting
join 131
join 140
sorting
sorting
join 143
sorting

出力例2
3
3
5
5
6

"""


import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
P = int(data[2])

# Read the initial heights of the students
index = 3
heights = []
for _ in range(N):
    heights.append(int(data[index]))
    index += 1

# Result list to capture positions of paiza-kun during sorting events
results = []



# Process the events
for _ in range(K):
    event = data[index]
    if event == "sorting":
        all_heights = heights + [P]
        all_heights.sort()
        position = all_heights.index(P) + 1
        results.append(str(position))
    elif event.startswith("join"):
        new_height = int(data[index + 1])
        heights.append(new_height)
        index += 1
    index += 1

# Print all the positions captured during sorting events
print("\n".join(results))
