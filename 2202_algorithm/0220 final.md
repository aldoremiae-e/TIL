# 0220 3차 과목평가 화이팅

## List1

- 알고리즘
- 배열
- 버블 정렬
- 카운팅 정렬
- 완전검색
- 그리디



### 알고리즘

> 컴퓨터가 어떠한 일을 수행하기 위한 단계적 방법, 어떠한 문제를 해결하기 위한 절차

- APS 과정의 목표 : 보다 좋은 알고리즘을 이해하고 활용하는 것!

  - 좋은 알고리즘 : 정확성! 작업량! 메모리 사용량! 단순성! 최적성!

  - 시간 복잡도
    - 빅 오 표기법 : 시간 복잡도 함수 중 가장 큰 영향력을 주는 n에 대한 항만 표시



### 배열

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

#### 배열 활용 예제 : Gravity

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 나보다 같거나 높은 칸이 있으면 낙차 정지
    # 나보다 작은 칸이 몇개나 있는가? -> 낙차 높이일것
    # 개수중에 가장 큰애
    max_num = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
            if cnt > max_num:
                max_num = cnt
    print(f'#{tc} {max_num}')
```

- 나보다 오른쪽에 있는 애들 중 나보다 작은애들의 개수만큼 떨어질 것
  - 나보다 오른쪽 :  j의 범위는 i+1 부터 끝까지
- 제일 큰 것:
  - cnt보다 전에 초기화가 되어야 함. 그래야 변하지 않고 저장됨



### 정렬

> 2개 이상의 자료를 특정 기준에 의해 순서대로 재배열 하는 것

- 배운 것 : 버블정렬, 카운팅 정렬, 선택정렬
- 아직 안배운 것 : 퀵 정렬, 삽입정렬, 병합정렬



- 버블정렬 : 인접한 두 개의 원소를 비교하여 정렬

  - 시간복잡도 O(n^)

  ```python
  '''[55 7 78 12 42] 오름차순 정렬'''
  
  arr = [55, 7, 78, 12, 42]
  # 배열의 마지막 인덱스부터
  for i in range(len(arr)-1, 0, -1):
      # 왼쪽 원소들을 차례로 비교, i번째 전까지
      for j in range(i):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]
          print(arr)
      print('-'*25)
  ```

  ```
  [7, 55, 78, 12, 42]
  [7, 55, 78, 12, 42]
  [7, 55, 12, 78, 42]
  [7, 55, 12, 42, 78]
  -------------------------
  [7, 55, 12, 42, 78]
  [7, 12, 55, 42, 78]
  [7, 12, 42, 55, 78]
  -------------------------
  [7, 12, 42, 55, 78]
  [7, 12, 42, 55, 78]
  -------------------------
  [7, 12, 42, 55, 78]
  -------------------------
  ```

  

- 카운팅 정렬 : 각 항목에 몇개씩 있는지 세는 작업을 통해 정렬

  - 시간복잡도 O(n+k) : n-리스트 길이, k- 정수의 최댓값

  ```python
  '''카운팅 정렬'''
  
  arr = [0, 4, 1, 3, 1, 2, 4, 1]
  count = [0 for _ in range(10)]
  result = [0 for _ in range(len(arr))]
  
  # 개수만큼 인덱스에 +1
  for i in range(len(arr)):
      count[arr[i]] += 1
  # count 배열의 원소를 누적값으로 갱신
  for j in range(1, len(count)):
      count[j] += count[j-1]
      print(count)
  
  #  result에 삽입
  for num in arr:
      idx = count[num]
      result[idx-1] = num
      count[num] -= 1
      print(result)
      print('-'*25)
  ```

  ```
  [0, 0, 0, 0, 0, 0, 0, 0]
  -------------------------
  [0, 0, 0, 0, 0, 0, 0, 4]
  -------------------------
  [0, 0, 0, 1, 0, 0, 0, 4]
  -------------------------
  [0, 0, 0, 1, 0, 3, 0, 4]
  -------------------------
  [0, 0, 1, 1, 0, 3, 0, 4]
  -------------------------
  [0, 0, 1, 1, 2, 3, 0, 4]
  -------------------------
  [0, 0, 1, 1, 2, 3, 4, 4]
  -------------------------
  [0, 1, 1, 1, 2, 3, 4, 4]
  -------------------------
  ```



### 탐욕 알고리즘

> 최적해를 구하는 데 사용되는 근시안적인 방법 - 그 순간 최적이라고 생각되는 것을 선택해 나가는 방식 ( 해 선택 - 실행 가능성 검사 - 해 검사 )

#### count 배열 예제 : baby-gin (greedy)

```python
T = int(input())
for tc in range(1, T+1):
    num = list(map(int, (input())))

    # 카운팅 정렬 이용
    cnt = [0 for _ in range(10)]
    for i in num:
        cnt[i+1] += 1

    # tri
    tri = 0
    for j in range(10):
        if cnt[j] >= 3:
           tri += 1
           cnt[j] -= 3

    # run
    run = 0
    for j in range(8):
        if cnt[j] > 0 and cnt[j+1] > 0 and cnt[j+2] > 0:
            run += 1
            cnt[j] -= 1
            cnt[j+1] -= 1
            cnt[j+2] -= 1

    if tri+run == 2:
        print('baby-gin')
    else:
        print('lose')
```



### 완전검색 (Brute-force)

> 완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법 -> 수행 속도는 느리지만, 해답을 찾아낼 확률이 높다

- {1, 2, 3}을 포함하는 순열

  ```python
  for i in range(1, 4):
      for j in range(1, 4):
          if i != j:
              for k in range(1, 4):
                  if k != i and k != j:
                      print(i, j, k)
  ```

  ```
  1 2 3
  1 3 2
  2 1 3
  2 3 1
  3 1 2
  3 2 1
  ```

  

## List2

- 2차원 배열
- 부분집합 생성
- 바이너리 서치
- 셀렉션 알고리즘
- 선택 정렬



### 2차원 배열 쓰는법

- 띄어쓰기 있을 때

  ```python
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  ----------------------------------------------------------
  3
  1 2 3
  4 5 6
  7 8 9
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

- 띄어쓰기 없을 때

  ```python
  N = int(input())
  arr = [list(map(int, input())) for _ in range(N)]
  ---------------------------------------------------------
  3
  123
  456
  789
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

  

- 열 우선 순회 =>

  ```python
  for i in range(N):
      for j in range(N):
          print(arr[i][j], end=' ')
      print()
  -------------------------------------------------------
  3
  123
  456
  789
  1 2 3 
  4 5 6 
  7 8 9 
  ```

- 지그재그 순회

  ```python
  for i in range(N):
      for j in range(N):
          # i가 짝수일때는 j
          # 홀수일때는 N-1-j
          print(arr[i][j + (N-1-2*j) * (i%2)], end=' ')
      print()
  ----------------------------------------------------
  3
  123
  456
  789
  1 2 3 
  6 5 4 
  7 8 9  
  ```

- 전치 행렬

  ```python
  for i in range(N):
      for j in range(N):
          if i < j:
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
      print(arr[i])
  ----------------------------------------------------------
  3
  123
  456
  789
  [1, 4, 7]
  [2, 5, 8]
  [3, 6, 9]
  ```



#### 연습문제1 - 델타행렬

```python
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    total = 0
    # 인덱스 주의
    for i in range(N):
        for j in range(N):
            for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    total += abs(arr[ni][nj]-arr[i][j])
    print(total)

---------------------------------------------------------------
1
5
45 15 10 56 23 
96 98 99 40 69 
96 84 49 46 34 
16 64 81 4 11 
10 66 85 55 14
#1 2430
```



### 부분집합

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for p in range(2):
                bit[3] = p
                print(bit)
```

```
[0, 0, 0, 0]
[0, 0, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 1]
[0, 1, 0, 0]
[0, 1, 0, 1]
[0, 1, 1, 0]
[0, 1, 1, 1]
[1, 0, 0, 0]
[1, 0, 0, 1]
[1, 0, 1, 0]
[1, 0, 1, 1]
[1, 1, 0, 0]
[1, 1, 0, 1]
[1, 1, 1, 0]
[1, 1, 1, 1]
```



- 연습문제2 - 부분집합 합이 0 되는게 있냐

  ```python
  T = int(input())
  for tc in range(1, T+1):
      N = 10
      arr = list(map(int, input().split()))
  
      # 부분집합 만들기
      for i in range(1, 1 << N): # 공집합 제외
          tot = 0
          for j in range(N):
              if i & (1 << j):
                  tot += arr[j]
          if tot == 0:
              print(f'#{tc} 1')
              break
      else:
          print(f'#{tc} 0')
  ```

  

### 이진탐색

> 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색 위치를 결정하고 검색을 계속 진행하는 방법 , 자료가 정렬되어 있어야 한다!

```python
def binarySearch(n, key):
    left = 1
    right = n
    cnt = 1
    while left <= right:
        c = int((left + right) / 2)
        if c == key:
            return cnt
        elif c > key: # c-1일수도 있음
            right = c
        else:
            left = c # c+1일수도 있음
        cnt += 1
    return False


T = int(input())
for tc in range(1, T + 1):
    page, pa, pb = map(int, input().split())

    a = binarySearch(page, pa)
    b = binarySearch(page, pb)

    if a < b:
        print(f'#{tc} A')
    elif a == b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
```



### 선택정렬

> 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환

```python
'''선택정렬'''
def selc(arr):
    N = len(arr)
    for i in range(N):
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return(arr)

lst = [64, 25, 10, 22, 11]
print(selc(lst))
-------------------------------------------------------
[10, 64, 25, 22, 11]
[10, 11, 64, 25, 22]
[10, 11, 22, 64, 25]
[10, 11, 22, 25, 64]
[10, 11, 22, 25, 64]
```



- 연습문제 - 달팽이

  ```python
  for tc in range(1,11):
      N = int(input())
      arr = [[0 for _ in range(N)] for _ in range(N)]
      row = 0
      col = -1
      num = 1
      trans = 1
      while N > 0:
          for i in range(N):
              col += trans
              arr[row][col] = num
              num += 1
          N -= 1
          for j in range(N):
              row += trans
              arr[row][col] = num
              num += 1
          trans *= -1
  
      print(f'#{tc}')
      for i in arr:
          for j in i:
              print(j, end=' ')
          print()
  ```

  
