#1부터 1000까지 나열

counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    
    else:
        print(n)
print(f'Divided {counter} times')