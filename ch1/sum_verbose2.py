print('Compute sum from a to b')

a = int(input("Enter an int a: "))
b = int(input("Enter an int b: "))

if a > b:
    a, b = b, a #a가 작도록 오름차순 정렬
#for 문 안의 조건문은 가능하면 밖으로 빼는 것이 효율적임
sum = 0
for i in range(a,b):
    print(f'{i} + ', end = '')
    sum += i
print(f'{b} = ', end ='')
sum += b
print(sum)