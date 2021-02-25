# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 01:48:01 2021

@author: newave986.git
"""

# page 262 "Telegram" 전보
# Shortest Algorithm - Dijkstra

import heapq

INF = int(1e9)
 
N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z])
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)
    