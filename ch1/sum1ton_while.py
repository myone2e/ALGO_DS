from re import I


print("Compute Summation from 1 to n")
n = int(input("Enter a Postive int: "))
if n < 0:
    print("Enter Positive int!!")
    n = int(input("Enter Again: "))

sum = 0 #초기화
i = 1

while i <= n:
    sum += i
    i += 1

print(f'sum of 1 to n is {sum}')
print(f'i = {i} & n = {n}') # i > n. i로 반복을 제어. 카운터 변수라고 부름