def recur(n):
    
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2) # 이렇게 recursive call 여러번 하는 것: 순수 재귀 (genuinely recursion)

x = int(input("Enter a int : "))
recur(x)