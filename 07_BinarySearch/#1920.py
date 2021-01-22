# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:51:28 2021

@author: newave986.git
"""

#BOJ 1920 수 찾기 - 이분 탐색

import sys
# sys.stdin.readline()

def binarysearch(array, key, start, end):
    middle = (start + end) // 2
    
    if start > end:
        return None 
    
    if array[middle] == key:
        return middle
    elif array[middle] < key:
        return binarysearch(array, key, middle + 1, end)
    else:
        return binarysearch(array, key, start, middle - 1)
    
n = int(sys.stdin.readline())
n_array = list(map(int, sys.stdin.readline().split()))
n_array.sort()

m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

for i in m_array:
    result = binarysearch(n_array, i, 0, n-1)
    
    if result == None:
        print('0')
    else:
        print('1')