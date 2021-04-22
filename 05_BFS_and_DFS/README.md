# Chapter 05. DFS/BFS
#### 탐색 알고리즘 Search Algorithm


|   |DFS|BFS|
|:---:|:---:|:---:|
|Used Structure|stack|queue|
|Implementation Method|recursive function|queue structure|


## [DFS *Dept First Search*]

- Dept First Search
- Visit node as deep as possible, and return to search another route.


### Basic Structure of **Graph**

- Graph consists of Node/Edge.
	- Node == Vertex

- Two nodes are "Adjanct": two nodes are connected by edge.


#### Ways to discribe Graph

 Adjancency Matrix: To express the connection relationship of a graph in a two dimensional array.

- 2차원 배열에 각 노드가 연결된 형태 기록.

- 연결되어 있지 않은 노드끼리는 무한Infinify의 비용이라고 작성.

- 값을 초기화할 때 논리적으로 정답이 될 수 없는 값으로 초기화.


Adjancency Matrix Example.py

```python
INF = 999999999 # 무한 비용 선언

graph = [
	[0, 7, 5],
	[7, 0, INF],
	[5, INF, 0]
	]
```




Adjancency List: To express the connection relationship of a graph in list.

- 인접 리스트: 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장

- '연결 리스트'라는 자료구조를 이용하여 구현


Ajcancency List Example.py

```python

# 행Row이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 - (노드, 거리) 형식으로
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph[2].append((0, 5))
```



#### Memory / Fast

인접 행렬 방식

- 모든 관계 저장 → 노드 갯수 많을수록 메모리 불필요하게 낭비됨


인접 리스트 방식

- 연결된 정보만 저장 → 메모리 효율적 사용

- 특정 두 노드가 연결되어 있는지에 대한 정보 얻는 속도 느림

- 특정 노드와 연결된 모든 인접 노드를 순회해야 하는 경우, 인접 리스트 > 인접 행렬 메모리 공간 낭비 적음




### DFS의 구체적인 동작

stack 자료 구조 이용

1. 탐색 시작 노드를 스택에 삽입 후 방문 처리

2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 함. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄

3. 2번의 과정을 더 이상 수행 불가할 때까지 반복



DFS Example.py

```python

# define DFS method
def dfs(graph, v, visited):
	# mark current node visited
	visited[v] = True
	print(v, end= ' ')
	# visit other nodes recursively which are connected with current node
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# show connected information as list structure (2 dimensional list)
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 7],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# show visited information as list structure (1 dimensional list)
visited = [False] * 9

# call defined DFS method
dfs(graph, 1, visited)
```




## [DFS *Dept First Search*]

- Breadth First Search

- Start to search with closest node


deque 라이브러리 사용하는 것이 좋음
탐색 수행함에 있어 O(N)의 시간 소요됨
DFS보다 BFS 구현이 조금 더 빠르게 구현됨
재귀 함수로 DFS 구현하면 느려질 수 잇음




### DFS의 구체적인 동작

queue 자료 구조 이용

1. 탐색 시작 노드를 큐에 삽입 후 방문 처리

2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리함

3. 2번의 과정을 더 이상 수행 불가할 때까지 반복




BFS example.py

```python

from collections import deque

# define BFS method
def bfs(graph, start, visited):
	# use deque library to implement queue
	queue = deque([start])
	# mark current node visited
	visit[start] = True
	# repeat until queue is empty
	while queue:
		# pick out one at queue and print it
		v = queue.popleft()
		print(v, end = ' ')
		# append ones that are connected with current nodes and not visited yet
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# show connected information as list structure (2 dimensional list)
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 7],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# show visited information as list structure (1 dimensional list)
visited = [False] * 9

# call defined DFS method
bfs(graph, 1, visited)
```

- Think 1 dim list & 2 dim list as **Graph**.
- Think search prob at 2 dim list into Graph prob.
