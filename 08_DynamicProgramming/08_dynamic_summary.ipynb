{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 다이나믹 프로그래밍 Dynamic Programming\n",
    "#### a.k.a 동적 계획법\n",
    "#### 중복되는 연산 줄이기\n",
    "#### 최적의 해를 구하기에 시간이 매우 많이 필요하거나 메모리 공간이 매우 많이 필요한 문제 등 -> 컴퓨터의 연산 속도의 한계 O, 메모리 공간을 사용할 수 있는 데이터의 개수도 한정적임 -> 제약 발생\n",
    "#### --> 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 작성해야 함\n",
    "#### 탑다운/보텀업 두 가지 방식 존재\n",
    "#### + 메모이제이션 기법 자주 함께 사용됨"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-3b0715729fc9>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mfibo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m \u001b[1;33m-\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mfibo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m \u001b[1;33m-\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfibo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'x' is not defined"
     ]
    }
   ],
   "source": [
    "# 8-1.py 피보나치 함수 소스코드\n",
    "\n",
    "# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현\n",
    "def fibo(x):\n",
    "    if x == 1 or x == 2:\n",
    "        return 1\n",
    "    return fibo(x - 1) + fibo(x - 2)\n",
    "\n",
    "print(fibo(x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### f(n) 함수에서 n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어남\n",
    "#### 동일한 함수가 반복적으로 호출됨"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 다이나믹 프로그램을 사용할 수 있는 조건\n",
    "#### 1. 큰 문제를 작은 문제로 나눌 수 있다.\n",
    "#### 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.\n",
    "#### \n",
    "#### Fibonacci 수열 문제를 메모이제이션Memoization 기법을 사용하여 해결할 수 있다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### \n",
    "### 메모이제이션 Memoization\n",
    "#### - 다이나믹 프로그래밍을 구현하는 방법 중 한 종류\n",
    "#### 한 번 구한 결과를 메모리 공간에 메모해 두고, 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법\n",
    "#### 메모이제이션은 값을 저장하는 방법이므로 캐싱Caching이라고도 함.\n",
    "#### \n",
    "#### 실재로 구현 방법: 한 번 구한 정보를 리스트에 저장\n",
    "#### 다이나믹 프로그래밍을 재귀적으로 수행하다가 같은 정보가 필요할 때에는 이미 구한 방법을 그대로 리스트에서 가져오면 됨\n",
    "#### 때에 따라서 다른 자료형(ex. dict)을 이용할 수 있음 -> 사전 자료형은 수열처럼 연속적이지 않은 경우에 유용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 8-2 py 피보나치 수열 소스코드(재귀적)\n",
    "\n",
    "# 한 번 계산된 결과를 메모이제이션Memoization 하기 위한 리스트 초기화\n",
    "d = [0] * 100\n",
    "\n",
    "# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)\n",
    "def fibo(x):\n",
    "    # 종료 조건(1 혹은 2일 때 1을 반환)\n",
    "    if x == 1 or x == 2:\n",
    "        return 1\n",
    "    # 이미 계산한 적 있는 문제라면 그대로 반환\n",
    "    if d[x] != 0:\n",
    "        return d[x]\n",
    "    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환\n",
    "    d[x] = fibo(x-1) + fibo(x-2)\n",
    "    return d[x]\n",
    "\n",
    "print(fibo(99))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 다이나믹 프로그래밍: 큰 문제라면 작게 나누고 / 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결\n",
    "#### - 큰 문제를 작게 나누는 방법: 퀵 정렬, 다이나믹 프로그래밍\n",
    "#### 퀵 정렬: Divide and Conquer 알고리즘으로 분류, 정렬을 수행할 때 정렬할 리스트를 분할하며 전체적으로 정렬이 될 수 있도록 함\n",
    "#### ex) 한 번 기준 원소Pivot가 자리를 변경하여 자리를 잡게 되면 그 기준 원소의 위치는 더 이상 바뀌지 않고 그 피벗값을 *다시 처리하는 부분 문제는 존재하지 않음*.\n",
    "#### <-> 다이나믹 프로그래밍: 문제들이 *서로 영향*을 미치고 있음\n",
    "#### 한 번 해결했던 문제를 다시금 해결 --> 이미 해결된 부분 문제에 대한 답을 저장해 놓고 이 문제는 이미 해결이 되었던 것이니까 다시 해결할 필요가 없다고 반환함.\n",
    "#### (-) 재귀 함수를 사용 -> 컴퓨터 시스템에서는 함수를 다시 호출했을 때 메모리 상에 적재되는 일련의 과정 따라야 함 -> 오버헤드 발생 가능\n",
    "#### --> 재귀 함수 대신 *반복문* 사용하여 오버헤드 줄일 수 있음\n",
    "#### 다이나믹 프로그램 적용 시 피보나치 수열 알고리즘의 시간 복잡도: O(N)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) "
     ]
    },
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 8-3.py 호출되는 함수 확인\n",
    "\n",
    "d = [0] * 100\n",
    "\n",
    "def pibo(x):\n",
    "    print('f(' + str(x) + ')', end = ' ')\n",
    "    if x == 1 or x == 2:\n",
    "        return 1\n",
    "    if d[x] != 0:\n",
    "        return d[x]\n",
    "    d[x] = pibo(x-1) + pibo(x-2)\n",
    "    return d[x]\n",
    "\n",
    "pibo(6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 탑다운 Top-Down 방식\n",
    "#### *재귀 함수*를 이용하여 다이나믹 프로그래밍 소스 코드를 작성하는 방법. 큰 문제를 해결하기 위해 작은 문제를 호출한다.\n",
    "#### 하항식\n",
    "#### 메모이제이션은 탑다운 방식에 국한되어 사용하는 표현\n",
    "#### --> 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미하므로 다이나믹 프로그래밍과는 별도의 개념. (다이나믹 프로그래밍과 꼭 함께 쓰이지 않아도 됨)\n",
    "### 보텀업 Bottom-Up 방식\n",
    "#### *단순히 반복문*을 이용하여 소스코드를 작성하는 경우. 작은 문제부터 차근차근 답을 도출한다.\n",
    "#### 상향식\n",
    "#### 결과 저장용 리스트: 'DP 테이블'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "218922995834555169026\n"
     ]
    }
   ],
   "source": [
    "# 8-4.py 피보나치 수열 소스 코드(반복적)\n",
    "\n",
    "# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화\n",
    "d = [0] * 100\n",
    "\n",
    "# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1\n",
    "d[1] = 1\n",
    "d[2] = 1\n",
    "n = 99\n",
    "\n",
    "# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)\n",
    "for i in range(3, n + 1):\n",
    "    d[i] = d[i-1] + d[i-2]\n",
    "\n",
    "print(d[n])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### 문제 풀이 단계의 1st. 주어진 문제가 다이나믹 프로그래밍 유형임을 파악\n",
    "#### ㄴ 특정 문제를 완전 탐색 알고리즘으로 접근했을 때 시간이 매우 오래 걸리면 다이나믹 프로그래밍을 적용할 수 있는지 해결하고자 하는 부분 문제들의 중복 여부 확인\n",
    "#### 메모이제이션을 적용할 수 있으면 코드를 개선하는 방법도 좋은 아이디어\n",
    "#### 가능하면 보텀업 방식 구현 권장 <- 재귀 함수의 스택 크기가 한정되어 있을 수 있음\n",
    "#### sys 라이브러리에 포함되어 있는 recursion setrecursionlimit() 함수를 호출하여 재귀 제한을 완화할 수 있음"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
