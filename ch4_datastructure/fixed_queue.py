# Fifo
# Using Ring Buffer => 시계 방향으로 인덱스 증가
class FixedQueue:
    
    # 예외처리 클라스 2개
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, capacity):
        
        self.no = 0 # 현재 데이터 갯수
        self.front = 0 # 맨 앞 원소 커서
        self.rear = 0 # 맨 끝 원소 커서
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐의 본체
        
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.no <= 0
    
    def is_full(self):
        return self.no >= self.capacity
    
    def enque(self, x):
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = x
        self.rear += 1 # 다음 원소 받을 곳으로 옮기기 (링 버퍼 생각)
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def deque(self, x):
        if self.is_empty():
            raise FixedQueue.Full
        x = self.que[self.front]
        self.front += 1 # 하나 빠짐 (시계 방향 기억)
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
        
    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front] # 가장 위쪽 원소를 제시
    
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity # front 값에 따라서 탐색 위치가 변함
            if self.que[idx] == value:
                return idx
        return -1 
    
    def count(self, value):
        cnt = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                cnt += 1
        return cnt
    
    def __contains__(self, value):
        return self.count(value)
    
    def clear(self):
        self.no = self.front = self.rear = 0
        
    def dump(self):
        if self.is_empty():
            print("The Que is empty")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front)%self.capacity], end='')
            print()