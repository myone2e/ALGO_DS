from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
        else:
            return -1
        
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