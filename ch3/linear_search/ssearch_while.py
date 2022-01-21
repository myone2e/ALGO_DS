from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input('Enter number of elements : '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('Enter key to search : '))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print('The key does not exist')
    else:
        print(f'Key value is at x[{idx}]')