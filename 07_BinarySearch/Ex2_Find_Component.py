# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:50:21 2021

@author: newave986.git
"""

# this is coding test with python - book exercise
# chapter 07 binary search
# exercise 02 find component

def binary_search(array, start, end, target):
    
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if target == array[mid]:
        return mid
    
    if target < array[mid]:
        return binary_search(array, start, mid - 1, target)
        
    else:
        return binary_search(array, mid + 1, end, target)
        

# import sys
# input = sys.stdin.readline

N = int(input())
stock = list(map(int, input().split()))
stock.sort()

M = int(input())
require = list(map(int, input().split()))

for i in require:
    if binary_search(stock, 0, N-1, i) == None:
        print("no", end = " ")
    else:
        print("yes", end = " ")
