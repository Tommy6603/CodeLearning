""""
整数 N が入力として与えられます。

1からNまでの整数を1から順に表示してください。

ただし、表示しようとしている数値が、

・3の倍数かつ5の倍数のときには、"Fizz Buzz"
・3の倍数のときには、"Fizz"
・5の倍数のときには、"Buzz"

を数値の代わりに表示してください。
"""

N = int(input("Type any integers : "))
for i in range(1, N + 1):

    if ((i % 3) == 0) & ((i % 5) == 0) : 
        print("Fizz Buzz")

    elif (i % 3) == 0 : 
        print("Fizz")

    elif (i % 5) == 0 : 
        print("Buzz")
    
    else : print(i)


    
