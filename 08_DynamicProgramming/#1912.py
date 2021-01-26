# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:56:58 2021

@author: newave986.git
"""

# BOJ 1912 연속합 - 다이나믹 프로그래밍 / 동적 계획법

# 런타임 에러 -> BOJ에 제출할 때 import sys 안 넣어서... babo....

# import sys
# sys.stdin.readline()

def continuous_sum(x):
    
    d = [0] * (x)
    d[0] = array[0]
    
    for i in range(x):
        d[i] = max(array[i] + d[i-1], array[i])
    
    return max(d)
    
n = int(input())
array = list(map(int, (input().split())))

if n == 1:
    print(array[0])
else:
    print(continuous_sum(n))





