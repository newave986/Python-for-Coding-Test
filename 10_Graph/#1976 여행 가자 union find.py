# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:58:01 2021

@author: @newave986.git
"""
# !! union parent, find parent 과정에서 자꾸 none 값이 리턴되는데
# 왜 그런지.. 어디를 고쳐야 하는지... 

# https://www.acmicpc.net/problem/1976
# BOJ 1976 여행 가자
# Union Find Problem

# import sys
# input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    else:
        return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    

N = int(input())
M = int(input())
graph = []
status = 0
parent = [i for i in range(N + 1)]

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    
goal = list(map(int, input().split()))


for i in range(N):
    for j in range(N-int(i/2)):
        if graph[i][j] == 1:
            print(parent)
            if parent[i] != parent[j]:
                union_parent(parent, i, j)
            

for k in range(len(goal) - 1):
    if parent[goal[k] - 1] != parent[goal[k+1] - 1]:
        status = 1
        break
        
print(parent)

if status == 0: print("YES")
else: print("NO")










