# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:54:57 2021
Changed on Wed Jan 27 11:32    2021

@author: newave986.git
"""

# runtime error
             
# import sys
# sys.stdin.readline()

from collections import deque

def make_level(x):

    global status
    
    queue = deque()
    queue.append(x)
    level[x] = 1
    
    while queue:
        
        k = queue.popleft()
    
        for t in my_list[k]:
                    
            if level[t] == 0:
                level[t] = -level[k]
                queue.append(t)
                    
            elif level[t] == level[k]:
                 status = False
                 return 0
             
    return 1      

num = int(input())

for k in range(num):
    
    ver, edg = map(int, input().split())
    my_list = [[] for _ in range(ver+1)]
    
    for i in range(edg):
        a, b = map(int, input().split())
        my_list[a].append(b)
        my_list[b].append(a)
    
    level = [0 for _ in range(ver + 1)]
    level[0] = 1
    status = True
    
    for l in range(1, ver+1):
            if status != False:
                if level[l] == 0:
                    make_level(l)
                    
    if 0 in level: status == False
    
    if status == False: print("NO")
    else: print("YES")




    
