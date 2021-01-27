# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:54:57 2021
Changed on Wed Jan 27 11:32    2021

@author: newave986.git
"""

# runtime error

def make_level():
    
    global queue
    global status
    
    while queue:
        
        k = queue.popleft()
    
        for t in my_list[k]:
                    
            if level[t] == 0:
                level[t] = -level[k]
                queue.append(t)
                    
            elif level[t] == level[k]:
                 status = False
                 break
             
# import sys
# sys.stdin.readline()

from collections import deque

num = int(input())

for k in range(num):
    
    ver, edg = map(int, input().split())
    my_list = [[] for _ in range(ver+1)]
    queue = deque()
    
    for i in range(edg):
        a, b = map(int, input().split())
        my_list[a].append(b)
        my_list[b].append(a)
    
    level = [0 for _ in range(ver + 1)]
    level[0] = 1
    status = True
    
    queue.append(1)
    level[1] = 1
    
    make_level()
             
    for l in level:
        if l == 0:
            queue.apped(l)
            level[l] = 1
            make_level()
    
    if 0 in level:
        status = False
    
    if status == False: print("NO")
    else: print("YES")
