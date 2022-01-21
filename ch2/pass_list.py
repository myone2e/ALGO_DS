def change(lst, idx, val):
    
    lst[idx] = val

x = [11, 22, 33, 44 , 55]
print('x =', x)

index = int(input('Choose an index to update : '))
value = int(input('To which value ? '))

change(x, index, value)
print(f'x = {x}')