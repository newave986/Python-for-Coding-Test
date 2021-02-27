# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 02:27:15 2021

@author: newave986.git
"""

# https://www.acmicpc.net/problem/11404
# BOJ #11404 Floyd-Warshall Algorithm

# import sys
# input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    # 왜 그냥 graph[a][b] = c라고 하면 프로그램이 잘못 돌아가고
    # min(graph[a][b], c)라고 해야 정답이 뜨는가
    
def Floyd():

    global n    
    global graph
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
Floyd()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    