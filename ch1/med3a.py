def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and a <= c):
        return a
    elif (a > b and c > b) or (c > b and a < b): # b >= a 가 이미 아니라서 elif 왔는데 한 번 더하니 비효율적인 코드
        return b
    else:
        return c
print("Get the median of 3 ints")
a = int(input("Enter int a: "))
b = int(input("Enter int b: "))
c = int(input("Enter int c: "))

print(f'The median is {med3(a,b,c)}')