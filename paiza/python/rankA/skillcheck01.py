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
    
    # data organization
    n = int(data[0])  # whole days of running
    k = int(data[1])  # How long campaign is(forget exact days)
    visitors = list(map(int, data[2:]))  # visiters list for each day (type of list)

    # sum of visiters for k days(Sliding-window method)
    # initialize of sliding-window
    current_sum = sum(visitors[:k])  # initial sum during k days
    max_sum = current_sum  # sum of maximum visitors
    count = 1  # times to appear the maximum sum
    earliest_start = 1  # sum of 0th and 1st day has already been culculated

    # main part of sliding-window
    for i in range(k, n):
        current_sum += visitors[i] - visitors[i - k] # minus element of the furthest on the left
        if current_sum > max_sum: #update
            max_sum = current_sum
            count = 1 # reset
            earliest_start = i - k + 2  # starting date for the updated maximum one(1-indexed)
        elif current_sum == max_sum:
            count += 1

    print(count, earliest_start)

find_best_campaign_period()