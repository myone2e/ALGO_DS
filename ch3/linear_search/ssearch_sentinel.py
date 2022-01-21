# Sentinel Method : 마지막에 보초를 세워 if문 하나를 제거
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) ->int:
    
    a = copy.deepcopy(seq)
    a.append(key)
    
    i = 0
    while True:
        if a[i] == key:
            break
        i +=1
    return -1 if i ==len(seq) else i

if __name__ == '__main__':
    num = int(input('Enter Number of Elements : '))
    x = [None] * num
    
    for i in range(num): #배열 먼저 입력 받고
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('Enter a key to search : '))
    
    idx = seq_search(x, ky) #검색 수행
    
    if idx == -1:
        print("The key does not exist")
    else:
        print(f'The key is at x[{idx}]')

