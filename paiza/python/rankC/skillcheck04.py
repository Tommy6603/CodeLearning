""""
宝くじ券には 100000 以上 199999 以下の 6 桁の番号がついています。毎年1つ当選番号 (100000 以上 199999 以下)が発表され、当たりクジの番号が以下のように決まります。

1等：当選番号と一致する番号
前後賞：当選番号の ±1 の番号（当選番号が 100000 または 199999 の場合，前後賞は一つしかありません）
2等：当選番号と下 4 桁が一致する番号（1等に該当する番号を除く）
3等：当選番号と下 3 桁が一致する番号（1等および2等に該当する番号を除く）

たとえば、当選番号が 142358 の場合、当たりの番号は以下のようになります。

1等：142358
前後賞：142357 と 142359
2等：102358, 112358, 122358, …, 192358 （全 9 個）
3等：100358, 101358, 102358, …, 199358 （全 90 個）

あなたが購入した n 枚の宝くじ券の各番号が入力されるので、それぞれの番号について、何等に当選したかを出力するプログラムを書いて下さい。

入力は以下のフォーマットで与えられます。

b
n
a_1
a_2
:
a_n

ここで、b は当選番号、n は購入した宝くじの数、a_1,…,a_n は購入した宝くじ券の番号をそれぞれ表します。


入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。

期待する出力
期待する出力は n 行から成ります。各 i 行目 (1 ≦ i ≦ n) には、a_i が何等に当たったかに応じて、以下の文字列を出力して下さい。

1等の場合: first
前後賞の場合: adjacent
2等の場合: second
3等の場合: third
それ以外（外れ）の場合: blank

最後は改行し、余計な文字、空行を含んではいけません。

"""

def check_lottery_numbers(b, tickets):
    results = [] #リストとして宣言
    
    # 1等の番号
    first_prize = b
    
    # 前後賞の番号
    if b == 100000:
        adjacent_prizes = [100001]#例外：100000の時は前後賞が１つしか存在しない
    elif b == 199999:
        adjacent_prizes = [199998]#例外：199999の時は前後賞が１つしか存在しない
    else:
        adjacent_prizes = [b - 1, b + 1]#通常
    
    # 2等の番号を生成 xに10〜19の数字(上２桁), B%10000で当選番号の下４桁
    second_prizes = [x * 10000 + b % 10000 for x in range(10, 20)]
    if b in second_prizes:
        second_prizes.remove(b)
    
    # 3等の番号を生成 xに100〜199の数字(上3桁), B%1000で当選番号の下3桁
    third_prizes = [x * 1000 + b % 1000 for x in range(100, 200)]
    third_prizes = [num for num in third_prizes if num not in second_prizes and num != b]#当選番号と２等の番号を除外
    
    # 各チケット番号について判定
    for ticket in tickets:
        if ticket == first_prize:
            results.append('first')
        elif ticket in adjacent_prizes:
            results.append('adjacent')
        elif ticket in second_prizes:
            results.append('second')
        elif ticket in third_prizes:
            results.append('third')
        else:
            results.append('blank')
    
    return results #リストは不変型なので戻す必要がある

import sys
input = sys.stdin.read
data = input().split()

b = int(data[0])
n = int(data[1])
tickets = list(map(int, data[2:2 + n]))
#map : 第一引数に指定された関数を第二引数に指定されたリストの各要素に適用。代入が必要。

results = check_lottery_numbers(b, tickets)
for result in results:
    print(result)