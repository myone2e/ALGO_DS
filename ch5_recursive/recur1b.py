import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# 현재 모듈의 절대경로를 알아내어 상위 폴더 절대경로를 참조 path에 추가하는 방식. 1단계 상위 폴더의 경로를 추가할 때 사용합니다.
from ch4_datastructure.stack import Stack # => 상위 경로에서 작업하는 것 처럼 

def recur(n):
    
    s = Stack(n)
    
    while True:
        if n > 0:
            s.push(n)
            n = n-1
            continue # stack에 4,3,2,1 들어감
        
        if not s.is_empty(): # 비어있지 않다면 마지막 값을 pop
            n = s.pop() # 1 pop
            print(n) # 1출력
            n = n - 2 # n = -1 되서 다시 맨 위로 => 2 pop하고 0되서 맨 위로 => 3 pop & n = 1되서 위로 가서 1 push ...
            continue
        
        break

x = int(input("Enter a int : "))
recur(x)