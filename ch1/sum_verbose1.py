print('Compute sum from a to b')

a = int(input("Enter an int a: "))
b = int(input("Enter an int b: "))

if a > b:
    a, b = b, a #a가 작도록 오름차순 정렬

sum = 0
for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end = '')
    sum += i
print(sum)