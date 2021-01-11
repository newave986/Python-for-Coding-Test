# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 04:01:54 2021

@author: newave986.git
"""

#1707 이분 그래프

import sys

num = int(input())

def appendToOneList(n):
    
    global my_list
    global one_list
    
    for k in my_list[n]:
        if k not in one_list:
            one_list.append(n)
            appendToOneList(k)
    
for k in range(num):
    
    ver, edg = map(int, sys.stdin.readline().split())
    my_list = [[] for _ in range(ver+1)]
    one_list = []
    
    for i in range(edg):
        a, b = map(int, sys.stdin.readline().split())
        my_list[a].append(b)
        my_list[b].append(a)
            
    appendToOneList(1)
    
    if len(one_list) == ver:
        print("NO")
    else:
        print("YES")
