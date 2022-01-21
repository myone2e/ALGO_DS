print('+- alternates')
n = int(input('How many? :'))

for i in range(n):
    if i % 2: #나머지 1
        print('-', end = '')
    else:
        print('+', end = '')
print()