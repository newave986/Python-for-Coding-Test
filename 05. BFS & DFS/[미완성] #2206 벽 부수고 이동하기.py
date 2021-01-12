# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 02:50:32 2021

@author: newave986.git
"""

# prob.
# 3차원 배열 이용하지 않고 2차원 배열으로, 특이 조건 걸어서 구현하고 싶으나
# if문이 안 돌아감은 물론 코드 전반적으로 문제가 있는 것으로 확인됨.
# 내가 하고 싶은 방법으로 구현할 방법은 없는지 조금 더 공부하는 것이 필요.


# BOJ 2206

from collections import deque

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

graph[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    
    status = 0
    
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        block = 0
        
        print(graph)

        for t in range(4):
            
            nx = x + dx[t]
            ny = y + dy[t]
            
            if nx < 0 or ny < 0 or nx >= x or ny >= y:
                continue
                
            if graph[nx][ny] == 1:
                continue
                
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                block += 1
        
        if block == 0: status += 1
        
        if status == 1:
            
            for j in range(4):
                
                kx = x + dx[j]
                ky = y + dy[j]
                
                if kx < 0 or ky < 0 or kx >= x or ky >= y:
                    pass
                    
                if graph[kx][ky] == 1:
                    graph[kx][ky] = graph[x][y] + 1
    
    if status > 2 or graph[x][y] == 0:
        return -1
    
    return graph[x][y]
    
print(BFS())
    
