# 🐣Begginner_Coder



## 1291 구구단

```python
while 1:
    s, e = map(int, input().split())
    if 1 < s < 10 and 1 < e < 10:
        if s < e:
            for i in range(1, 10):
                for j in range(s, e+1):
                    print('{0} * {1} = {2:>2}'.format(j, i, j*i), end='   ')
                print()
            break
        else:
            for i in range(1, 10):
                for j in range(s, e-1, -1):
                    print('{0} * {1} = {2:>2}'.format(j, i, j*i), end='   ')
                print()
            break
    else:
        print("INPUT ERROR!")

```

```
# 입력
4 3
```

```
# 출력
4 * 1 =  4   3 * 1 =  3
4 * 2 =  8   3 * 2 =  6
4 * 3 = 12   3 * 3 =  9
4 * 4 = 16   3 * 4 = 12
4 * 5 = 20   3 * 5 = 15
4 * 6 = 24   3 * 6 = 18
4 * 7 = 28   3 * 7 = 21
4 * 8 = 32   3 * 8 = 24
4 * 9 = 36   3 * 9 = 27
```



## 1341 구구단2

```py
while 1:
    s, e = map(int, input().split())
    if 1 < s < 10 and 1 < e < 10:
        if s < e:
            for k in range(s, e+1):
                for i in range(1, 10):
                    print('{0} * {1} = {2:>2}'.format(k, i, k*i), end='   ')
                    if i % 3 == 0:
                        print()
                print()
            break
        else:
            for k in range(s, e-1, -1):
                for i in range(1, 10):
                    print('{0} * {1} = {2:>2}'.format(k, i, k*i), end='   ')
                    if i % 3 == 0:
                        print()
                print()
            break
```

```
# 입력
4 3
```

```
# 출력
4 * 1 =  4   4 * 2 =  8   4 * 3 = 12
4 * 4 = 16   4 * 5 = 20   4 * 6 = 24
4 * 7 = 28   4 * 8 = 32   4 * 9 = 36

3 * 1 =  3   3 * 2 =  6   3 * 3 =  9
3 * 4 = 12   3 * 5 = 15   3 * 6 = 18
3 * 7 = 21   3 * 8 = 24   3 * 9 = 27
```

