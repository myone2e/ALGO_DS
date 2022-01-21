print('+- alternates')
n = int(input('How many? :'))

for _ in range(n//2):
    print('+-', end='')
if n % 2:
    print('+', end='')
print()