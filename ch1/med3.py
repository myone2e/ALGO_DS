def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print("Get the median of 3 ints")
a = int(input("Enter int a: "))
b = int(input("Enter int b: "))
c = int(input("Enter int c: "))

print(f'The median is {med3(a,b,c)}')