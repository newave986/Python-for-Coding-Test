# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:56:55 2021

@author: newave986.git
"""

# BOJ 2805 나무 자르기 <- 이분 탐색

# import sys
# sys.stdin.readline()

def cut_tree(start, end):
    
    while start <= end:
        
        bring = 0
        mid = (start + end) // 2
    
        for i in tree_list:
            if mid < i:
                bring += i - mid
            else:
                pass
            
        if bring >= M:
            start = mid + 1
            
        else:
            end = mid - 1
    
    return end

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

print(cut_tree(0, tree_list[N-1]))
