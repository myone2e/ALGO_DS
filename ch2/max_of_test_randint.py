import random
from max import max_of

print('Compute Maximum of Random numbers')

num = int(input('How many? : '))
lo = int(input('Enter lower bound : '))
hi = int(input('Enter upper bound : '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo ,hi)

print(f'{x}')
print(f'Maximum in x is {max_of(x)}')