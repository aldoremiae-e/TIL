# IM 보충

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