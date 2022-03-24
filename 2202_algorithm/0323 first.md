# 0323 first



## 비트 연산자

| 연산자 | 연산자의 기능                                     |
| ------ | ------------------------------------------------- |
| &      | 비트단위로 AND 연산을 한다.                       |
| \|     | 비트단위로 OR 연산을 한다.                        |
| ^      | 비트단위로 XOR 연산을 한다. (같으면 0 다르면 1)   |
| ~      | 단항 연산자로서 피연산자의 모든 비트를 반전시킨다 |
| <<     | 피연산자의 비트 열을 왼쪽으로 이동시킨다.         |
| >>     | 피연산자의 비트 열을 오른쪽으로 이동시킨다.       |



### 1<<n

- 2^n의 값을 갖는다.
- 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
- Power set (모든 부분 집합)
  - 공집합과 자기 자신을 포함한 모든 부분집합
  - 각 원소가 포함되거나 포함되지 않는 2가지 경우의 수를 모든 부분집합의 수가 계산된다.



### i & (1 <<j)

- 계산 결과를 i의 j번째 비트가 1인지 아닌지를 의미

```python
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%2d = " %i , end='')
    Bbit_print(i)
```

```
-5 = 11111011
-4 = 11111100
-3 = 11111101
-2 = 11111110
-1 = 11111111
 0 = 00000000
 1 = 00000001
 2 = 00000010
 3 = 00000011
 4 = 00000100
 5 = 00000101
```



```python
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output,end=' ')

a = 0x10
x = 0x01020304
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i*8) & 0xff)
```

```
16 = 00010000 
01020304 = 00000100 00000011 00000010 00000001 
```



```python
def ce(n): # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p

x =0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i*8)) & 0xff)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
```

```
x = 4321
x = 1234
```

