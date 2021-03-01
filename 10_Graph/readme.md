Chapter 10. Graph Algorithm
=================
그래프 이론

> 9372 https://www.acmicpc.net/problem/9372
</br>

## 개요

- Graph: Node와 Node 사이에 연결된 Edge의 정보를 가지고 있는 자료구조
- '서로 다른 Object가 연결되어 있다'는 이야기를 들으면 가장 먼저 떠올릴 것.
- Tree(Graph) 자료 구조 기억
    - Priority Queue 구현할 때 Heap 사용 -> Min Heap은 트리 자료구조에 속함
    - 트리 자료구조: 부모에서 자식으로 내려오는 계층적인 모델
- DFS/BFS(Chapter 05), Shortest Path(Chapter 09) 모두 그래프 알고리즘의 한 유형
- Kruskal Algorithms: Greedy Algorithm
- Topology Algorithms: Use Queue/Stack Algorithm

|          | Graph | Tree |  
| -------- | :-----: | :-----: |  
|  방향성  |  방향/무방향 | 방향 |  
|  순환성  |  순환/비순환 | 비순환 |  
|  루트 노드 존재 여부  |  X | O |  
|  노드 간 관계성  | 부모-자식 관계 X | 부모-자식 관계 O |  
|  모델의 종류  |  네트워크 모델 | 계층 모델 |  



### 그래프 구현 방법
#### Adjancency Matrix 이용하는 방법과 Adjancency List 이용하는 방법이 있음.

|          | Adjancency Matrix | Adjancency List |  
| -------- | :-----: | :-----: |  
|  구현 방법  |  2차원 배열 | 리스트 |  
|  간선 정보 저장 시 필요한 메모리 공간 | O(V^2) | O(E) |  
|  특정 노드 A에서 다른 특정 노드 B로 이어진 간선의 비용 탐색 시 필요 시간 |  O(1) |  O(V) |  
|  이용 알고리즘  |  플로이드 워셜 알고리즘 | 다익스트라 최단 경로 알고리즘 |  

- Floyd Algorithm: Adjancency List 이용
    - 모든 노드에 대하여 다른 노드로 가는 최소 비용을 V^2 크기의 2차원 리스트로 저장한 뒤
    - 해당 비용 갱신하여 최단 거리 계산
- Dijkstra Algorithm: Priority Queue 이용
    - 노드의 개수가 V일 때는 V개의 리스트를 만들어서 각 노드와 연결된 모든 간선에 대한 정보를 리스트에 저장
- **메모리와 시간을 염두에 두고 알고리즘 선택하여 구현**
    - 노드의 개수가 적음: Floyd
    - 노드와 간선의 개수가 모두 많음: Dijkstra

## Disjoint Sets == Union-Find Data Structure
- 서로소 집합
    - 공통 원소가 없는 두 집합
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료 구조
- 두 집합이 서로소 관계인지 확인
    - == 각 집합이 어떤 원소를 공통으로 가지고 있는지 확인
- **Union**
    - 합집합 연산
    - 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
- **Find**
    - 찾기 연산
    - 특정한 원소가 속한 집합이 어떤 집합인지 알려 주는 연산
- 트리 자료구조를 이용하여 집합 표현

### 작동 원리
1. union 연산 확인
    - 서로 연결된 두 노드 A, B 확인
    - A와 B의 루트 노드 A', B' 각각 찾은 후
    - A'를 B'의 부모 노드로 설정(B'가 A'을 가리키도록 함)
2. 모든 union 연산을 처리할 때까지 1번 과정 반복

- A', B' 중에서 더 번호가 작은 원소가 부모 노드가 되도록 구현
- union의 관계를 효과적으로 보여 주기 위해 그래프 형태로 표현될 수 있음
- 트리 구조상 번호가 작은 노드가 부모 노드, 번호가 큰 노드가 자식 노드가 됨
- union 연산을 하나씩 확인하면서 서로 다른 두 원소에 대해 union을 수행해야 될 때는 각각 루트 노드를 찾아 더 큰 루트 노드가 더 작은 루트 노드를 가리키도록 하면 됨
- **'부모 테이블'** 항상 가지고 있어야 함
    - 모든 원소가 자기 자신을 부모로 가지도록 설정
    - *재귀*적으로 부모를 거슬러 올라가 최종 루트 노드를 찾아야 함
        - 부모 테이블을 계속해서 확인하며 거슬러 올라가야 함
        - ex) 노드 3의 부모 노드: 2, 노드 2의 부모 노드: 1 → 노드 3의 보무 노드: 1
        - 부모 노드인 2로 이동한 다음 노드 2의 부모를 또 확인해서 노드 1로 접근

### 기본적인 서로소 집합 알고리즘 구현
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각자 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = '')

print()
 
# 부모 테이블 내용 출력
print('부모 테이블: ', end = '')
for i in range(1, v + 1):
    print(parent[i], end = '')
```
- 루트 노드가 같은 원소끼리는 동일한 집합을 이룸

### Path Compression 경로 압축
- 위 기본적인 코드에서는 find 함수가 비효율적으로 동작
   - 최악의 경우, find 함수가 모든 노드를 다 확인 → 시간 복잡도가 O(V)
   - 노드의 개수가 V개이고 find & union 연산의 개수가 M개일 때 → 시간 복잡도가 O(VM)
- Path Compression으로 find 함수 최적화
    - find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신하는 기법

```python
# 경로 압축 기법 소스 코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
```

- 각 노드에 대하여 find 함수 호출 이후에 해당 노드의 루트 노드가 부모 노드가 됨
- 루트 노드에 더욱 빠르게 접근할 수 있다는 점에서 시간 복잡도 개선됨

### 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 무방향 그래프 내에서의 사이클 판별할 때 사용 가능
- 방향 그래프 사이클: DFS 이용하여 판별 가능
- 작동 원리 알고리즘
    - 각 간선을 확인하며 두 노드의 루트 노드 확인
        - 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산 수행
        - 루트 노드가 서로 같다면 Cycle 발생
    - 그래프가 포함되어 있는 모든 간선에 대하여 1번 과정 반복
- 그래프에 포함되어 있는 간선의 개수가 E개일 때, 모든 간선을 하나씩 확인 → 매 간선에 대하여 union 및 find 함수를 호출하는 방식으로 동작

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았따면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:   
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
```

























