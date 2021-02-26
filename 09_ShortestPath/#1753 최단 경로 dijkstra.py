# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:44:15 2021

@author: newave986.git
"""

# https://www.acmicpc.net/problem/1753
# BOJ #1753 Shortest Path

import heapq
import sys

INF = int(1e9)
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
length = [INF for _ in range(V + 1)]
for _ in range(E):
    u, v, m = list(map(int, sys.stdin.readline().split()))
    graph[u].append([v, m])


def Dijkstra(start):
    
    global length
    
    q = []
    
    length[start] = 0
    heapq.heappush(q, [0, start])
    
    while q:
        
        distance, vertex = heapq.heappop(q)
        
        if length[vertex] < distance:
            continue
        
        for i in graph[vertex]:
            if distance + i[1] < length[i[0]]:
                length[i[0]] = distance + i[1]
                heapq.heappush(q, [length[i[0]], i[0]])

Dijkstra(K)

for i in range(1, V + 1):
    if length[i] == INF:
        print("INF")
    else:
        print(length[i])








