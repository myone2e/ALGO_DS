from re import I


print('Compute sum of 1 to n')
#양수를 입력할 때 까지 계속 돌도록
while True:
    n = int(input('Enter n: '))
    if n > 0:
        break 
    
sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1
        
print(f'Sum of 1 to {n} is {sum}')