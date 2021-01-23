# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:06:50 2021

@author: newave986.git
"""

import sys 
#sys.stdin.readline()

def find_max_long(start, end):
    
    while start <= end:
        
        key = (start + end) // 2
        count = 0
    
        for i in range(K):
            count += array[i] // key
        
        if count >= N:
            # 조건에 맞는 key 값을 찾았더라도
            # key의 최댓값을 찾는 루프를 돌려야 함
            start = key + 1
            
        else:
            # 조건에 맞지 않으므로 다시 루프를 돌려야 함
            end = key - 1
        
    print(end)
        
K, N = map(int, sys.stdin.readline().split())
array = []

for _ in range(K):
    tmp = int(sys.stdin.readline())
    array.append(tmp)
    
array.sort()

find_max_long(1, array[K-1])
