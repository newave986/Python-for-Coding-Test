# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:39:43 2021

@author: newave986.git
"""

# BOJ 2667 단지 번호 붙이기

from collections import deque

# BFS 함수를 선언한다.
def BFS(graph, m, j):
    
    global status
    global visit
    global n
    
    visit[m][j] = True
    
    village = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    if graph[m][j] == 0:
        pass
    
    elif graph[m][j] == 1:
        
        status += 1
        queue = deque()
        queue.append((m, j))
    
        while queue:
            
            (x, y) = queue.popleft()
            
            for r in range(4):
                
                rx = x + dx[r]
                ry = y + dy[r]
                
                if 0 <= rx < n and 0 <= ry < n and visit[rx][ry] == False:
                    visit[rx][ry] = True
                    
                    if graph[rx][ry] == 1:
                        queue.append((rx, ry))
                        village += 1
                        
        return village + 1

# 지도의 크기와 지도를 입력받는다.
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
ans = []
status = 0

# 방문한 노드를 체크하는 visit 리스트를 만든다.
visit = [[False for _ in range(n+1)] for _ in range(n + 1)]

# 지도를 탐색한다.
for m in range(n):
    for j in range(n):
        if visit[m][j] == False:
            k = BFS(graph, m, j)
            if type(k) is int:
                ans.append(k)

ans.sort()

print(status)
for t in range(len(ans)):
    print(ans[t])
