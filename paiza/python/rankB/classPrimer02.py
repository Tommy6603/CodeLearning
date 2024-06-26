"""
居酒屋で働きながらクラスの勉強をしていたあなたは、お客さんをクラスに見立てることで勤務時間中の店内の人数や注文の情報を管理できることに気付きました。
全てのお客さんは、ソフトドリンクと食事を頼むことができます。加えて 20 歳以上のお客さんはお酒を頼むことができます。
20 歳未満のお客さんがお酒を頼もうとした場合はその注文は取り消されます。
また、お酒（ビールを含む）を頼んだ場合、以降の全ての食事の注文 が毎回 200 円引きになります。

今回、この居酒屋でビールフェスをやることになり、ビールの注文が相次いだため、いちいちビールの値段である 500 円を書くのをやめ、注文の種類と値段を書く代わりに 0 とだけを書くことになりました。

勤務時間の初めに店内にいるお客さんの人数と与えられる入力の回数、各注文をしたお客さんの番号とその内容、または退店したお客さんの番号が与えられます。
お客さんが退店する場合はそのお客さんの会計を出力してください。勤務時間中に退店した全てのお客さんの会計を出力したのち、勤務時間中に退店した客の人数を出力してください。

入力される値
N K
a_1
...
a_N
n_1 o_1
...
n_K o_K


・ 1 行目では、お客さんの人数 N と入力の回数 K が与えられます。
・ 続く N 行のうち i 行目(1 ≦ i ≦ N)では、i 番目のお客さんの年齢が与えられます。
・ 続く K 行では、頼んだお客さんの番号 n_i , 注文を表す文字列 o_i が与えられます。
・ o_i では、注文の種類 s_i と 値段 m_i (1 ≦ i ≦ K) を表す文字列 "s_i m_i" または、ビールの注文を表す "0" または、そのお客さんが会計を行い帰ることを表す "A" が与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。

期待する出力
sum_1
...
C


お客さんが帰るたびにそのお客さんの会計を出力してください。 1 人の会計ごとに改行を行ってください。
勤務時間中に帰った全てのお客さんの会計を出力したのち、勤務時間中に退店した客の人数 C を出力してください。
条件
・ 1 ≦ N , K ≦ 1000
・ 1 ≦ a_i ≦ 100 (1 ≦ i ≦ N)
・ 1 ≦ n_i ≦ N (1 ≦ i ≦ K)

o_i (1 ≦ i ≦ K) は次のうちのいずれかの形式です。

・ "s_i m_i"
1 ≦ s_i ≦ N (1 ≦ i ≦ K) は "food" , "softdrink" , "alcohol" のいずれかです。
food , softdrink , alcohol はその注文が食事・ソフトドリンク・お酒であることを表しています。また、300 ≦ m_i ≦ 5000 です。

・ "0"
その注文がビールであることを表す。

・ "A"
n_i 番のお客さんが会計をして退店することを表す。

入力例1
2 3
20
30
1 0
2 0
1 A

出力例1
500
1

"""

class Customer:
    def __init__(self, age):
        self.age = age
        self.total_bill = 0
        self.discount_active = False

    def order(self, item, price=0):
        if item == "alcohol" or item == "0":
            if self.age < 20:
                return  # 未成年はお酒を注文できない
            if item == "0":
                price = 500  # ビールの固定価格
            self.discount_active = True  # お酒を注文したら割引をアクティブにする
        if item == "food" and self.discount_active:
            price -= 200  # 割引適用
            if price < 0:
                price = 0  # 価格がマイナスにならないように
        self.total_bill += price

    def checkout(self):
        return self.total_bill

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    K = int(data[index])
    index += 1
    
    customers = []
    
    for _ in range(N):
        age = int(data[index])
        index += 1
        customers.append(Customer(age))
    
    bills = []
    
    for _ in range(K):
        n_i = int(data[index]) - 1  # 顧客番号（0ベースインデックス）
        o_i = data[index + 1]
        index += 2
        
        if o_i == "A":
            # 顧客が退店して会計を行う
            bill = customers[n_i].checkout()
            bills.append(bill)
        elif o_i == "0":
            # ビールの注文
            customers[n_i].order("0")
        else:
            # その他の注文
            order_type, price = o_i, int(data[index])
            index += 1
            customers[n_i].order(order_type, price)
    
    # 結果の出力
    for bill in bills:
        print(bill)
    print(len(bills))  # 退店した顧客の数

if __name__ == "__main__":
    main()
