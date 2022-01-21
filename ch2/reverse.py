from typing import Any, MutableSequence

#list.reverse() 역할. inplace

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('Reverse the array elements')
    nx = int(input('How many elements? : '))
    x = [None] * nx
    
    for i in range(nx):
        x[i] = int(input(f'Enter value of x[{i}] : '))
        
    reverse_array(x)
        
    print("Reversed the array elements")
    
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
        