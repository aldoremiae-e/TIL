

# 0221 stack

## Stack 

> 마지막에 삽입한 자료를 가장 먼저 꺼낸다

- 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산
  - 자료구조 : 자료를 선형으로 저장할 저장소
    - 배열 사용 가능
    - 저장소 자체를 스택이라고 부르기도 함
    - Stack pointer : 스택에서 마지막 삽입된 원소의 위치를 top이라 부름

- 스택의 삽입/ 삭제 과정
  - push : top을 증가시키고 그자리에다가 값을 넣는다
    - append 메소드를 통해 리스트의 마지막에 데이터를 삽이부 
  - pop : top에 있는 걸 지우고 top을 감소시킨다 (지운다기 보다는 덮는다)

- 스택은 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만

  스택의 크리를 변경하기 어렵다는 단점이 있다 

  => 동적 연결리스트를 이용하며 극복


```python
# 삽입할 자료를 매개변수로
def push(item):
    # top증가 -> top위치에 자료를 넣음 : 리스트의 마지막 원소에 추가하는 append메서드 활용
    # python의 list는 크기의 제한이 없기 때문에 overflow 문제 해결    
    s.append(item)
def pop():
    # top이 -1이면 스택에 자료가 없는 상태
    # 리스트의 크기를 len을 통해 알 수 있어 top의 변수 필요 없음
    if len(s)==0:
        #underfloor
        return
    # stack의 마지막 값을 반환
    # top위치에 있는 값을 리턴함 -> 리스트의 마지막 값을 삭제하고 뽑아오는 pop 메서드 활용
    else:
        return s.pop(-1)
s = []
push(1)
push(2)
push(3)
print("pop item =>", pop()) # pop item => 3
print("pop item =>", pop()) # pop item => 2
print("pop item =>", pop()) # pop item => 1
```



- 괄호검사

  

## Memoization

> 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록하여 전체적인 실행속도를 빠르게 하는 기술

- 재귀 함수로 만들면 엄청난 중복 호출을 해야한다는 단점을 보완

- DP의 핵심!

피보나치 수열

```python
def fibo(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

N= 10
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))		#55
print(memo)			#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```



## DP  동적 프로그래밍

> Dynamic Programming 최적화 문제를 해결하는 알고리즘

- 문제를 부분 문제로 분할한다.
- 부분 문제로 나누는 일을 끝냈으면 가장 작은 문제부터 해를 구한다
- 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.

피보나치 수열

```python
N= 10
fibo = [0]*(N+1)
fibo[0] = 0
fibo[1] = 1
for i in range(2, N+1):
    fibo[i] = fibo[i-1] +fibo[i-2]

print(fibo) 		#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```



- 재귀 vs Memo

| 재귀 Recursive                                               | 반복 Memoization                                       |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| 내부에 시스템 호출 스택을 사용하는 **overhead**가 발생할 수 있음 | 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적 |

