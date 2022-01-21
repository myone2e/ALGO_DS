from typing import Any, Sequence

def bin_search(a, key):
    
    pl = 0
    pr = len(a) - 1 #n-1
    
    while True:
        pc = (pl + pr) // 2 #center
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('Enter Number of Elements: '))
    x = [None] * num
    
    print('Enter datas in ascending order!')
    
    x[0] = int(input(f'x[0]: '))
    
    for i in range(1, num):
        while True: #smaller value 들어오면 다시 받도록 하기 위해서!
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('Enter a key to search: '))
    
    idx = bin_search(x, ky)
    
    if idx == -1:
        print('The key does not exist')
    else:
        print(f'The key is at x[{idx}]')
    