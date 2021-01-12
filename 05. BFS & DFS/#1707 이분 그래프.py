# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 04:01:54 2021

@author: newave986.git
"""

# 1707 이분 그래프
# BFS와 트리의 정의를 이용하여야 한다.
# "이진트리"에서, 같은 레벨의 노드는 서로 연결될 수 없다. 
# 집합을 둘로 분할하여야 하므로 2 레벨의 트리일 것.
# 일단 레벨을 부여하는 것은 필요해 보인다. 
# test case 1) 에서, 3은 lv 1의 노드(1, 2의 부모 노드) 이고 1,2는 lv 2의 노드로 3의 자식 노드임.
# 그럼 자식 노드로 분류한 다음 자식 노드끼리 같은 레벨을 가진다고 하면 false 출력해야겠네.

import sys as sys
from collections import deque

num = int(sys.stdin.readline())

for k in range(num):
    
    ver, edg = map(int, sys.stdin.readline().split())
    my_list = [[] for _ in range(ver+1)]
    queue = deque()
    
    for i in range(edg):
        a, b = map(int, sys.stdin.readline().split())
        my_list[a].append(b)
        my_list[b].append(a)
    
    visited = [False for _ in range(ver + 1)]
    level = [0 for _ in range(ver + 1)]
    status = True
    
    queue.append(1)
    level[1] = 1
    
    while queue:
        
        k = queue.popleft()
    
        for t in my_list[k]:
            if visited[t] == False:
                queue.append(t)
                    
            if level[t] == 0:
                 level[t] = -level[k]
                    
            elif level[t] == level[k]:
                 status = False
                 break
    
    if status == False: print("NO")
    else: print("YES")
