print('print *')
n = int(input("Total stars? :"))
w = int(input("How many stars in each line? :"))
#w개 출력하고 줄바꿈
for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()
        
#마지막 줄 처리
if n % w:
    print()