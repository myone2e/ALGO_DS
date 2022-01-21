from ssearch_while import seq_search

print('Search for a Real Number.')
print('Warnings: "End" ends the program!')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1
    
ky = float(input('Enter a value to search: '))

idx = seq_search(x, ky)
if idx == -1:
    print('The key does not exist!')
else:
    print(f'The key is at x[{idx}]')