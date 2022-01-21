n = int(input('Enter a short length: '))
for i in range(n):
    for _ in range(n-i-1):
        print(' ', end = '')
    for _ in range( i + 1 ):
        print('*', end ='')
    print()