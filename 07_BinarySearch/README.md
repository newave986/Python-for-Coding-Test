# Chapter 07. 이진 탐색
#### 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘


## [순차 탐색 Sequential Search]

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로-순차로- 확인-데이터를 탐색-하는 방법

- 보통 *정렬되지 않은 리스트*에서 데이터를 찾아야 할 때 사용

- 리스트 내에 데이터가 아무리 많아도 시간이 충분하다면 항상 원하는 원소 찾을 수 있음

- 리스트의 데이터에 하나씩 방문하며 특정한 문자열과 같은지 검사하므로 구현도 간단함

- count() 메서드를 이용할 때에도 내부에서는 순차 탐색이 수행됨

- 데이터의 개수가 N 개일 때 최대 N 번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N)


## 순차 탐색 소스 코드

### 순차 탐색 소스 코드 구현

```python

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) 
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

```

> 생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요. </br>
5 Dongbin </br>
앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다. </br>
Hanul Jonggu Dongbin Taeil Sangwook </br>
3



## [이진 탐색 Binary Search] 

- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘

- 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있음

- 탐색 범위를 반으로 좁혀가며 데이터를 탐색함


- 시작점, 끝점, 중간점(반내림)의 변수 3개 이용함

- 찾으려는 데이터와 중간점Middle 위치에 있는 데이터를 반복적으로 비교하여 원하는 데이터를 찾는 게 이진 탐색 과정

-  한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)


## 재귀 함수로 구현한 이진 탐색 코드

### 이진 탐색 소스 코드 구현 (재귀 함수)

```python

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

```

> 10 7 </br>
1 3 5 7 9 11 13 15 17 19 </br>
4

## 반복문으로 구현한 이진 탐색 코드

### 이진 탐색 코드 구현(반복문)

```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간값 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

- 코딩 테스트에서 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많음.
	- 따라서 탐색 범위가 2,000만을 넘어서면 이진 탐색으로 문제에 접근해 보아야 함.



## [트리 자료구조]

이진 탐색의 전제 조건: 데이터 정렬

데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리Tree 자료 구조를 이용하여 항상 데이터가 정렬되어 있음.
	
따라서 데이터베이스에서의 탐색은 이진 탐색과는 조금 다르지만, 이진 탐색과 유사한 방법을 이용해 탐색을 항상 빠르게 수행하도록 설계되어 있어서 데이터가 많아도 탐색하는 속도 빠름.

- 1) 트리는 부모 노드 - 자식 노드의 관계로 표현됨

- 2) 트리의 최상단 노드: 루트 노드

- 3) 트리의 최하단 노드: 단말 노드

- 4) 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 함

- 5) 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합함


 
## [이진 탐색 트리]

트리 자료구조 중 가장 간단한 형태가 이진 탐색 트리임.

-  1) 부모 노드보다 왼쪽 자식 노드가 작다.

- 2) 부모 노드보다 오른쪽 자식 노드가 크다.

	-  ==> 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

```python
# 빠르게 입력받기

import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
# 입력받은 문자열 그대로 출력
print(input_data)
```