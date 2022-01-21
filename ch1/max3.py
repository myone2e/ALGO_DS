from re import A


print("Get Maximum value of 3 ints")
a = int(input("Enter int a: "))
b = int(input("Enter int b: "))
c = int(input("Enter int c: "))

maximum = a
#sequential structure (순차 구조): 한 문장씩 순서대로 처리되는 구조
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c

print(f'The maximum value is {maximum}')