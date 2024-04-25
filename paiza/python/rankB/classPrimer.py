"""
クラスの学級委員である paiza 君は、クラスのみんなに次のような形式でアカウントの情報を送ってもらうよう依頼しました。

名前 年齢 誕生日 出身地

送ってもらったデータを使いやすいように整理したいと思った paiza 君はクラス全員分のデータを次の形式でまとめることにしました。

User{
    nickname : 名前
    old : 年齢
    birth : 誕生日
    state : 出身地
}


途中で名前が変わった際にいちいちデータを修正するのが面倒だと思ったあなたは、生徒の構造体と新しい名前を受け取り、その名前を修正する関数 changeName を作成し、それを用いて生徒の名前を更新することにしました。

クラスの人数と全員の情報、更新についての情報が与えられるので、入力に従って名前を更新した後のクラスのメンバーの情報を出力してください。

入力される値
N K
n_1 o_1 b_1 s_1
...
n_N o_N b_N s_N
a_1 nn_1
...
a_K nn_K


・ 1 行目では、paiza君のクラスの人数 N と名前更新の回数 K が与えられます。
・ 続く N 行のうち i 行目 (1 ≦ i ≦ N) では、 i 番の生徒の名前・年齢・誕生日・出身地を表す整数・文字列 n_i ,o_i ,b_i , s_i が順に半角スペース区切りで与えられます。
・ 続く K 行では、名前を更新する生徒の番号 a_i と、その人の新しい名前 nn_i が空白区切りで与えられます。

入力値最終行の末尾に改行が１つ入ります。
文字列は標準入力から渡されます。 

期待する出力
n_1 o_1 b_1 s_1
...
n_N o_N b_N s_N

入力例1
1 1
koko 23 04/10 tokyo
1 nana

出力例1
nana 23 04/10 tokyo

入力例2
3 2
mako 13 08/08 nara
taisei 16 12/04 nagano
megumi 14 11/02 saitama
2 taihei
3 megu

出力例2
mako 13 08/08 nara
taihei 16 12/04 nagano
megu 14 11/02 saitama

"""

class User: # class定義
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state

def changeName(user, new_nickname): #userクラスのデータとchar型を受け取る
    user.nickname = new_nickname

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    # 1行目の入力: N と K を読み込む
    first_line = data[0].split()
    N = int(first_line[0])
    K = int(first_line[1])
    
    # 学生データの読み込み
    students = [] #リストとして定義
    for i in range(1, N + 1):
        n_i, o_i, b_i, s_i = data[i].split()
        student = User(nickname=n_i, old=o_i, birth=b_i, state=s_i) #Userクラスのインスタンスに格納
        students.append(student) #全体のリストに格納
    
    # 名前更新の指示の読み込み
    updates = data[N + 1:N + 1 + K] 
    for update in updates:
        if update:
            a_i, nn_i = update.split()
            a_i = int(a_i) - 1  # 0-based index
            changeName(students[a_i], nn_i) #名前変更関数(変更するのは名前だけ)
    
    # 更新後の学生情報の出力
    for student in students:
        print(f"{student.nickname} {student.old} {student.birth} {student.state}")

if __name__ == "__main__":
    main()
