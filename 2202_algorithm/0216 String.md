# 0216 문자열 (string)

> 각 문자에 대해서 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법

- 숫자에다가 문자의 의미를 주고 , 문자를 나타내는 표식과 함께 작성

## 문자 종류

- 아스키코드 : 7bit 인코딩으로 128문자를 표현함

- 유니코드 : 다국어 처리를 위해 만들어짐

- 엔디안 (endian)
  - big-endian 낮은 수를 높은 주소에 저장
  - little-endian 낮은 자리수를 빠른(낮은)주소에 저장

- 유니코드 인코딩 (UTF : Unicode Transformation Format)

  - 파이썬3.x버전은 UTF-8 사용

  

## 문자열의 분류

- java 언어에서의 문자열

- c언어에서의 문자열

- s1 = list(input()) 와 s2 = input() 차이

  ```python
  s1 = list(input()) 	# abc
  s2 = input()		# abc
  s1 += 'c'
  s2 += 'c'
  print(s1, type(s1))	# ['a', 'b', 'c', 'c'] <class 'list'>
  print(s2, type(s2)) # abcc <class 'str'>
  ```


  

- 문자열 세는 strlen() 를 직접 작성해보기

  ```python
  def my_strlen(a):
      cnt = 0
      i = 0
      while a[i] != '\0':
          i += 1
          cnt += 1
      return cnt
  
  s = ['a', 'b', 'c','\0']
  print(my_strlen(s))		#3
  ```



## 문자열 처리

- python 에서 문자열은 시퀀스 자료형으로 분류되고, immutable 하고 itterable 하다.
- 인덱싱, 슬라이싱 연산들을 사용할 수 있고, 문자열 클래스에서 제공되는 메소드가 있다.
  - replace() , split() , isalpha(), find() 등

- is 와 == 의 차이

  ```pyhton
  s1 = 'abc'
  s2 = 'abc'
  s3 = 'def'
  s4 = s1             # s1을 참조
  s5 = s1[:2] + 'c'   # s1의[:2]까지만 참조 + 다른 주소의 'c'참조
  
  print(s1 == s2)     # == 는 내용이 같을 때 True
  print(s1 is s2)     # is 는 같은 것을 참조할 때 True
  print(s1 is s4)		# True
  print(s1 == s5)		# True
  print(s1 is s5)		# False
  ```

- 문자열 뒤집기

  - 슬라이싱 이용하여 s[::-1]

    ```python
    a = 'abc'
    b = a[::-1]
    print(a , b)	# abc cba
    ```

  - s.reverse() # s가 리스트일때만 동작한다.

    ```python
    lst = ['a', 'b', 'c']
    lst.reverse()
    print(lst)		# ['c', 'b', 'a']
    ```

- 문자열 비교

  - c 언어 : atoi() 제공

  - java : parse 메소드 제공

  - python : 숫자와 문자변환 함수 제공

    ```python
    a = 'a'
    b = 'b'
    c = 'A'
    if ord(a) > ord(b) :
        print(a, ord(a), b, ord(b)) 
    else:
        print(b, ord(b), a, ord(a)) 	# b 98 a 97
    
    if ord(a) > ord(c) :
        print(a, ord(a), c, ord(c))		# a 97 A 65
    else:
        print(c, ord(c), a, ord(a))
    ```



## 패턴매칭

### 고지식한 패턴매칭

```python
'''
연속된 1의 개수의 최댓값
'''

# 어떻게 입력값을 받을까?
N = int(input())		# 10
# 붙어들어오면 input() 띄어들어오면 input().split()
arr = list(map(int, input()))		# 0011000111
# 훑었을 때 1을 만나면 cnt 를 저장하도록 하고 0을 다시 만나면 0이 되야겠다.
maxV = 0
for i in range(N):
    if arr[i] == 0:
        cnt = 0
    if arr[i] == 1:
        cnt += 1
    # maxV 로 cnt를 비교해서 가장 큰 값을 찾도록
        if cnt > maxV:
            maxV = cnt
print(maxV)			# 3
```



### KMP 알고리즘 (lps)

- 시간복잡도 O(M+N)
  - 중복되는 부분을 제외하고 다른 부분부터 비교 시작

