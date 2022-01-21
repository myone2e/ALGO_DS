#시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

#sequence 자료형 a를 받아 any(제약이 없는 임의의 자료형) return
#annotation임 => 강제성은 없음!
#즉, 힌트를 주는 것이라 보면 됨
def max_of(a: Sequence) -> Any: 
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print("Get maximum of array")
    num = int(input("Number of elements? : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}] value is : '))
    print(f'The maximum is {max_of(x)} !')