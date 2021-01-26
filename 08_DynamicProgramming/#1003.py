# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:03:54 2021

@author: newave986.git
"""

# BOJ 1003 fibonnaci function <- Dynamic Programming Basic

# import sys
# sys.stdin.readline()

def fib(x):

    global zero_array, one_array, visit
    
    zero_array[0] = 1
    
    if x > 0:
        one_array[1] = 1
        
    if x > 1:
        zero_array[2] = 1
        one_array[2] = 1
        
    for i in range(3, x + 1):
        
        zero_array[i] = zero_array[i-1] + zero_array[i-2]
        one_array[i] = one_array[i-1] + one_array[i-2]
    
T = int(input())

for _ in range(T):
    
    N = int(input())
    one_array = [0] * (N+1)
    zero_array = [0] * (N+1)
    
    fib(N)
    
    print(zero_array[N], one_array[N])
