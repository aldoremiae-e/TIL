# IM 보충

- 11012 03_배열2_사각영역들의 합

- 2001
- 1209
- 11315 오목판정
- 1220 mag
- 3499 퍼팩트셔플
- 1860 진기의 최고급 붕어빵
- 2805
- 1974
- 1289

## 2차 배열에서 사각영역을 표현

- 색칠하기

  - 좌상단 좌표, 우하단 좌표

    ```python
    for r in range(r1. r2+1):
        for c cin range(c1, c2+1):
            arr[r][c]
    ```

- 파리퇴치

  - 좌상단 좌표, 너비, 높이

    ```python
    # h :높이 w:너비
    for r in range(r,r+h):
        for c in range(c,c+w):
    ```

    

- 구간합 : 패턴매칭, 파리퇴치, 회문 ...

  - 길이가 N인 배열에서 길이가 M인 가능한 모든 구간에 대해서 작업

- 패턴매칭

  - 텍스트에서 패턴이 존재하는 모든 위치를 찾는 문제

    ```python
    t = []
    p = []
    N, M = len(t), len(p)
    # i :텍스트 인덱스, j :패턴의 인덱스
    for i in range(N - M  + 1):
        # 길이가 M인 패턴 비교
        # 상태를 저장하는 변수
        flag = True
        for j in range(M):
            if t[i+j] != p[j]:
                flag = False
                break
        # 불일치로 끝난건지, 그냥 끝난건지
        # flag = False > break하면 끝난거임
        if flag:
            # t[i]에서 패턴을 찾았다.
        
    ```

    ```python
    t = []
    p = []
    N, M = len(t), len(p)
    # i :텍스트 인덱스, j :패턴의 인덱스
    for i in range(N - M  + 1):
        # 길이가 M인 패턴 비교
        
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            # t[i]에서 패턴을 찾았다.
    ```

    - 모든 패턴을 다 찾으려면 : while 문으로 건너뛸 수 있도록 만들도록!

    ```python
    while i < N-M+1 :
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else: # 아니면 건너 뛸 수 있도록
            i = i +M -1 # 아래 i가 더해지므로 1을 빼줘
        i += 1
    ```

    ------------------------------------------------------------------------------------------------------------------------



## 델타

델타 안쓰고

```python
N = 10
arr = [[0]*N for _ in range(N)]
r = c =7

# 우
for i in range(c+1, N):
    arr[r][i] = 1
# 하
for i in range(r + 1, N):
    arr[i][c] = 2
# 좌
for i in range(c-1,-1,-1):
    arr[r][i] = 3
# 상
for i in range(r-1,-1,-1):
    arr[i][c] = 4

for lst in arr:
    print(*lst)
```

```python
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 4 0 0
3 3 3 3 3 3 3 0 1 1
0 0 0 0 0 0 0 2 0 0
0 0 0 0 0 0 0 2 0 0
```

델타

```python
N = 10
arr = [[0]*N for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = c = 5

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    while (0 <= nr < N and 0 <= nc < N):
        arr[nr][nc] = i + 1
        nr = nr + dr[i]
        nc = nc + dc[i]
#            if nr < 0 or nr >= N or nr < 0 or nc >= N:
#                break


for lst in arr:
    print(*lst)
```



- 정수같은 immutable 한 애들은 변경불가능하기 때문에, 함수 내에 변경하려면 global 써야함
- 리스트같은 mutable 한 애들은 변경이 가능하기 때문에, 함수 내에서도 전역변수처럼 써도됨, 굳이 매개변수로 두지 않아도 됨!



```python
def row(arr, N):
    for i in range(N):
        for j in range(2,N-2):
            if arr[i][j-2] == 'o' and arr[i][j-1] == 'o' and arr[i][j] == 'o' and arr[i][j+1] == 'o' and arr[i][j+2] == 'o':
                return 1

    # 세로
def col(arr, N):
    for j in range(N):
        for i in range(2, N-2):
            if arr[i-2][j] == 'o' and arr[i-1][j] == 'o' and arr[i][j] == 'o'
    # 대각선
```



## 기지국

![image-20220225193702583](IM%20%EB%B3%B4%EC%B6%A9.assets/image-20220225193702583.png)

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                continue
            elif arr[i][j] == 'A':
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for di, dj in [[2, 0], [1, 0], [0, 2], [0, 1], [-2, 0], [-1, 0], [0, -2], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for di, dj in [[3, 0], [2, 0], [1, 0], [0, 3], [0, 2], [0, 1], [-3, 0], [-2, 0], [-1, 0], [0, -3], [0, -2], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 'H' and 0 <= ni < N and 0 <= nj < N:
                        arr[ni][nj] = 'X'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')
```

![image-20220225194855227](IM%20%EB%B3%B4%EC%B6%A9.assets/image-20220225194855227.png)

- 대신 오타나 이런거에 주의해야함
