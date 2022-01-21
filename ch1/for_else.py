import random

n = int(input("Enter a number for rands: "))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r ==13:
        print('\nEnd the program')
        break
else:
    print('\nEnd generating rands')