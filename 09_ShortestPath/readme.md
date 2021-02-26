Chapter 09. Shortest Path 
=================
최단 경로 알고리즘

1753 https://www.acmicpc.net/problem/1753 </br>
11404 https://www.acmicpc.net/problem/11404

## 개요
- 가장 짧은 경로를 찾는 알고리즘
- '길 찾기'
- 상황에 맞는 효율적인 알고리즘이 이미 정립되어 있음
- *최단 거리*를 출력하도록 요구하는 문제가 많이 출제됨

### 종류
- 다익스트라 최단 경로 알고리즘
- 플로이드 워셜
- 벨만 포드 알고리즘

## 다익스트라 최단 경로 알고리즘

### 작동 순서
1. 출발 노드 설정

2. 최단 거리 테이블 초기화
출발 노드의 거리는 1, 나머지 노드의 거리는 무한

3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택

4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
4번을 반복할 때 진행되는 것:

|인접 노드|현재값|거쳐갈 때|갱신 여부|
|:---:|:---:|:---:|:---:|
|3|5|1+3|True|
|5|무한|1+1|True|

5. 3번과 4번을 반복


### 특징
- 그리디 알고리즘
    - 매 상황에서 방문하지 않은, 가장 비용이 적은 노드를 선택하여 과정 반복함.
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정됨.
    - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것.
- 다익스트라 알고리즘 수행한 뒤 테이블에 각 노드까지의 최단 거리 정보 저장
    - 노드의 경로 구하려면 별도의 알고리즘 필요함

### 구현 방법
1. 각 노드에 대한 최단 거리를 담는 1차원 리스트 선언
2. 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색).

### **간단한** 다익스트라 알고리즘 소스 코드

```python
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억 설정, 무한 의미하는 값

# 노드의 수 n, 간선의 수 m
n, m = map(int, input().split())

# 시작 노드 번호 start
start = int(input)

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 graph
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 리스트 visited
visited = [False] * (n+1)

# 무한대로 초기화한 최단 거리 테이블 리스트 distance
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미이다.
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[i]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
- 시간 복잡도: O(V^2)
    - V is number of Nodes.
    - 총 O(V)번에 걸쳐 최단 거리가 가장 짧은 노드를 매번 **선형** 탐색, 현재 노드와 연결된 노드를 매번 일일이 확인
    - 노드의 개수가 10,000개를 넘어가는 문제라면 이 코드는 사용이 어려움
    - 따라서 노드의 개수 및 간선의 개수가 많을 때는 아래의 '개선된 다익스트라 알고리즘' 이용해야 함

--------

### **개선된** 다익스트라 알고리즘 

- 시간 복잡도: O(ElogV)
    - V is number of Nodes, E is number of Edges.
- 선형 탐색(간단한 다익스트라) 사용하지 않고 **힙Heap 자료구조** 사용.
    - 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리
    - 출발 노드로부터 가장 거리가 짧은 노드 더욱 빠르게 찾을 수 있음

### 힙 자료 구조 Heap Data Structure
- 우선 순위 큐 Priority Queue를 구현하기 위하여 사용하는 자료 구조 중 하나
    - 우선 순위 큐: 우선 순위가 가장 높은 데이터를 가장 먼저 삭제
    - 데이터를 우선 순위에 따라 처리하고 싶을 때 사용함
    - PriorityQueue, heapq 사용 가능
        - 일반적으로 *heapq*의 속도가 더 빠름
    - 첫 번째 원소를 기준으로 우선 순위를 설정
    - 하나의 데이터를 삽입 및 삭제할 때의 시간 복잡도는 O(logN)
- 단순 리스트로도 구현 가능

|우선순위 큐 구현 방식|삽입 시간|삭제 시간|
|:---:|:---:|:---:|:---:|
|리스트|O(1)|O(N)|
|힙(Heap)|O(logN)|O(logN)|

- 최소 힙Min Heap / 최대 힙Max Heap 사용
    - 최소 힙: 값이 낮은 데이터가 먼저 삭제됨
        - 힙에서 원소를 꺼내면 '가장 값이 작은 원소'가 추출됨
        - 파이썬 우선 순위 큐 라이브러리는 최소 힙에 기반
    - 최대 힙: 값이 높은 데이터가 먼저 삭제됨
    - 최소 힙을 최대 힙처럼 사용하기 위해 일부러 우선 순위에 해당하는 값에 음수 부호(-) -> 꺼낸 다음 다시 음수 부호(-) 붙여서 원래의 값으로 돌리는 방식 사용 가능

### 구현 방법
현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선 순위 큐를 추가로 이용</br>
시작 노드로부터 '거리'가 짧은 노드 순서대로 큐에서 나올 수 있도록 다익스트라 알고리즘 작성 </br>
최단 거리 테이블에 남아 있는 거리가 각 노드로의 최단 거리

### **개선된** 다익스트라 알고리즘 소스 코드
get_smallest_node() 함수를 작성할 필요가 없음</br>
최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체 가능</br>
```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억 설정, 무한 의미하는 값

# 노드의 수 n, 간선의 수 m
n, m = map(int, input().split())

# 시작 노드 번호 start
start = int(input)

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 graph
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 리스트 visited
visited = [False] * (n+1)

# 무한대로 초기화한 최단 거리 테이블 리스트 distance
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미이다.
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue:
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, cost, i[0])

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] = INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
```
시간 복잡도가 O(ElogV)로 기본적인 다익스트라 알고리즘보다 훨씬 빠르다.




















