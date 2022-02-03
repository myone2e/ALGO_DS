from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드 => 개별 해시값(버킷)을 나타냄"""
    
    def __init__(self, key, value, next): #any, any, Node, 결과 None
        """initialization"""
        self.key = key #key가 정수 등의 raw dats
        self.value = value #hash function applied = hash value
        self.next = next #다음 노드를 참조하는 포인터

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity):
        #Table 생성 (해시값 담을 곳) #해시값 = 버킷. ***Table은 해시값이 index.
        #***Table[4]에는 해시값이 4인 애들 중 head node를 참조하는 값이 저장됨 
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key): #any, int
        """해시값을 구함"""
        
        if isinstance(key, int): #key가 int라면 바로. #자료형 확인하는 함수
            return key % self.capacity
        #key가 int가 아닌 경우를 처리
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity)
    
    def search(self, key): #any, any
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash] #Head node를 참조하는 포인터 역할. 근데 얘는 버킷이자 노드
        
        while p is not None:
            if p.key == key: #검색 성공
                return p.value
            p = p.next
            
        return None #검색 실패
    
    def add(self, key, value): #결과 bool
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]
        
        #key값을 선형 검색해서 같은 키 값이 발견되면 추가 실패. 발견 안되면 맨 앞에 노드를 추가
        while p is not None:
            if p.key == key:
                return False #추가 실패
            p = p.next
            
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True #추가 성공
    
    def remove(self, key):
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key) #삭제할 key의 해시값
        p = self.table[hash] #노드를 주목
        pp = None #바로 앞 노드
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next #다음 노드를 대입해버림
                else:
                    pp.next = p.next 
                return True
            pp = p
            p = p.next
        return False
    
    def dump(self):
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'    -> {p.key} ({p.value})', end ='')
                p = p.next 
            print()