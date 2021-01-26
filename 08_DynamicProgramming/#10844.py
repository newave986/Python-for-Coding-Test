# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:47:38 2021

@author: newave986.git
"""

# BOJ 10844 계단 수 세기 <- 동적 계획법 / 다이나믹 프로그래밍

# import sys
# sys.stdin.readline()

def stair_number(x):
    
    global d
    
    for i in range(1, 10):
        d[0][i] = 1
        
    for i in range(1, N):
        for j in range(1, 9):
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
        d[i][0] = d[i-1][1]
        d[i][9] = d[i-1][8]
        
N = int(input())
d = [[0 for _ in range(10)] for _ in range(N)]
stair_number(N)
sum = 0

for k in range(10):
    sum += d[N-1][k]

print(sum%1000000000)