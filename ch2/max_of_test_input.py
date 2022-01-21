from max import max_of

print("Get maximum of array")
print("If you type 'End', program ends!")

number = 0
x = []

while True:
    s = input(f'Enter x[{number}] : ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'Entered total {number} numbers')
print(f'The maximum is {max_of(x)}')