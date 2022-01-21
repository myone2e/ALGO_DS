print('print *')
n = int(input("Total stars? :"))
w = int(input("How many stars in each line? :"))

for _ in range(n//w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)