
counter = 0 #효율성 체크용
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2): #only odd numbers
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0: #소수로 나눠지면 빠져나오고
            break
        else:
            prime[ptr] = n #안나눠지면 다음 소수로 시도
            ptr += 1
            
for i in range(ptr):
    print(prime[i])
    
print(f'Number of division: {counter}')