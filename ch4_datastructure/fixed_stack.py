from typing import Any
# LIFO = Python List
class FixedStack:
    
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, capacity):
        self.stk = [None] * capacity #스택의 본체
        self.capacity = capacity
        self.ptr = 0
        
    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0 # 스택이 비어있는지 판단
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self): #lst.pop([index])
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self): # 꼭대기를 들여다 본다
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self):
        self.ptr = 0
    
    def find(self, value):
        for i in range(self.ptr-1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value):
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                cnt += 1
        return cnt
    
    def __contains__(self, value):
        return self.count(value>0)
    
    def dump(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            print(self.stk[:self.ptr]) #바닥에서부터 꼭대기까지 출력 # lst[:len(lst)]
    