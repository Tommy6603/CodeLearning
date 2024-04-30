"""
あなたは、とあるウェブサイトを管理していました。
ある連続した k 日間、このウェブサイトでキャンペーンをおこなったのですが、いつからいつまでの期間におこなったかを忘れてしまいました。

幸い、ウェブサイトを運営していた全 n 日分のアクセスログが残っており、1 日ごとの訪問者数が分かっています。
とりあえず、連続する k 日の中で、1 日あたりの平均訪問者数が最も多い期間を、キャンペーンをおこなった期間の候補だと考えることにしました。

n 日分の訪問者数のリストとキャンペーンの日数 k が入力されるので、キャンペーンをおこなった期間の候補数と、候補の中で最も早い開始日を出力してください。

入力される値
入力は 2 行からなります。

1 行目には n と k が半角スペース区切りで入力されます。
2 行目には n 個の整数 a_1, a_2, …, a_n が半角スペース区切りで入力されます。a_i は i 日目の訪問者数を表します。
入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
キャンペーンをおこなった期間の候補数と、候補の中で最も早い開始日を、この順で半角スペース区切りで 1 行で出力してください。

条件
すべてのテストケースにおいて、以下の条件をみたします。
・1 ≦ n ≦ 300,000
・1 ≦ k ≦ n
・0 ≦ a_i ≦ 100

入力例1
5 3
1 2 3 2 1

出力例1
1 2

入力例2
10 2
6 2 0 7 1 3 5 3 2 6

出力例2
5 1
"""

def find_best_campaign_period():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 全日数
    k = int(data[1])  # キャンペーンの日数
    visitors = list(map(int, data[2:]))  # 各日の訪問者数のリスト

    # スライディングウィンドウ法で k 日間の訪問者の合計を計算
    current_sum = sum(visitors[:k])  # 最初の k 日間の合計
    max_sum = current_sum  # 最大の訪問者数の合計
    count = 1  # 最大合計が現れる回数
    earliest_start = 1  # 最初の k 日間が最大なので、開始日は 1

    for i in range(k, n):
        current_sum += visitors[i] - visitors[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            count = 1
            earliest_start = i - k + 2  # 新しい最大値の開始日 (1-indexed)
        elif current_sum == max_sum:
            count += 1

    print(count, earliest_start)

find_best_campaign_period()