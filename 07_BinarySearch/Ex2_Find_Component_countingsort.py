# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:18:31 2021

@author: newave986.git
"""

# this is coding test with python - book exercise
# chapter 07 binary search
# exercise 02 find component
# 계수 정렬으로 구현할 수도 있다!

stock = [0] * 1000001

import sys
input = sys.stdin.readline

N = int(input())

for i in input().split():
    stock[int(i)] = 1
stock.sort()

M = int(input())
require = list(map(int, input().split()))

for j in require:
    if stock[j] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")