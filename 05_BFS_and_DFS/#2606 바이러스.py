# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:34:56 2021

@author: newave986.git
"""

# BOJ 2606

num1 = int(input())
num2 = int(input())

connect = [[] for _ in range(num1 + 1)]
virus = [1]

for i in range(num2):
    a, b = map(int, input().split())
    if b not in connect[a]:
        connect[a].append(b)
    if a not in connect[b]:
        connect[b].append(a)
    
def DFS(num):
    global virus
    global connect
    
    for i in connect[num]:
        if i not in virus:
            virus.append(i)
            DFS(i)

DFS(virus[0])
print(len(virus) - 1)
