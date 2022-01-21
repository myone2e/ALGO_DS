print('Compute sum from a to b')

a = int(input("Enter an int a: "))
b = int(input("Enter an int b: "))

if a > b:
    a, b = b, a #a가 작도록 오름차순 정렬

sum = 0 
for i in range(a, b+1):
    sum += i

print(f'sum of {a} to {b} is {sum}')