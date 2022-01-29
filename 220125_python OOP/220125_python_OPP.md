# 220126_python_OPP

## 객체 지향 프로그래밍 

> 파이썬은 모두 객체(object)로 이루어져 있다.

- 객체(object)는 특정 타입의 인스턴스(instance)이다.
  - 객체 : 타입(type) 속성(attribute) 조작법(method)

- 객체 지향 프로그래밍이란?	

  - 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
  - 데이터(type)과 기능(method)를 분리하여 추상화된 구조(인터페이스)를 구축

  ```
  객체 지향의 장점 -위키피티아-
  프로그램을 유연하고 변경이 용이하게 만들 수 있어 대규모 소프트웨어 개발에 많이 사용된다.
  프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수가 간편하고
  보다 직관적인 코드 분석이 가능하다.
  ```



### OOP기초

> 기본문법

1. 클래스 정의	2. 인스턴스 생성	3. 메소드 호출 	4. 속성

- 클래스와 인스턴스 : 클래스 (객체의 틀)을 가지고, 객체(인스턴스)를 생성

- 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미

- 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위 (함수)

  ```python
  #Person 이라는 클래스를 생성
  class Person:
      pass
  
  #Person 클래스의 인스턴스를 ssafykim 이라는 변수에 저장
  ssafykim = Person() 
  
  # 변수 ssafykim이 Person클래스의 인스턴스인지 확인?
  isinstance(ssafykim, Person) # => True
  
  # 타입
  print(type(ssafykim)) # => <class '__main__.Person'>
  ```



### 인스턴스

> 인스턴스 변수

- 인스턴스가 개인적으로 가지고 있는 속성

- 각 인스턴스들의 고유한 변수

- 정의 : 생성자 메소드에서 self.<name>

- 접근 및 할당 : 인스턴스가 생성된 이후 <instance>.<name>

  ```python
  # 변수명 정의
  ssafykim.name = 'miae'
  print(ssafykim.name)
  ```



> 인스턴스 메소드

- 인스턴스 변수를 사용하거나, 인스턴스 변소에 값을 설정하는 메소드
- 클래스 내부에 정의되는 메소드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

```python
class Person:
    def talk(self):
        print('안녕!')
    def eat(self, food):
        print(f'냠냠 {food}')
# Person클래스의 인스턴스를 p1에 저장
p1 = Person()
# 클래스 내부의 메소드를 사용하는 방법
p1.talk() # => 안녕!
p1.eat('김밥') # => 냠냠 김밥
p1.eat('햄버거') # => 냠냠 햄버거
```



> self

- 인스턴스 자기자신
- 인스턴스 메소드 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계

```python
class Person:
    def test(self):
        print(self)
p1 = Person()
# 메서드 호출시 첫 번째 인자로 인스턴스 자신이 전달
p1.test() # => <__main__.Person object at 0x000001C83E675D30>
print(p1) # => <__main__.Person object at 0x000001C83E675D30>
```



> 생성자 메소드

- 인스턴스 객체가 **생성될 때 자동으로 호출되는** 메소드
- 인스턴스 변수들의 초깃값을 설정
  - 인스턴스 생성
  - `_ _init_ _` 메소드 자동 호출

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'I am {self.name}')
        
# self 변수명을 인자로 넘기는 __init__ 바로 호출, Person의 인스턴스 p1의 변수명을 'tom'으로 생성
p1 = Person('tom')
# talk 메서드 실행
p1.talk() # => I am tom
```

```python
# talk 메서드를 클래스에서 메서드를 실행해봅시다. self는 정말 빈자리일까요?
뭔소리임
# =====
Person.talk(p1) # => I am tom
```



> 소멸자 메소드

- 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
- `_ _del_ _` 이라는 이름으로 정의한다.

```python
class Person:
    def __init__(self):
        print('응애!')
        
    def __del__(self):
        print('떠날게..')
# Person 클래스의 인스턴스 생성 => p1 변수에 저장    
# 생성자 메소드를 통해 자동으로 응애 함
p1 = Person() # => 응애!
# del 키워드를 이용해 소멸자를 활용
del p1 # => 떠날게..
```



> 매직 메소드

- 더블 언더바가 있는 메소드는 특수한 동작을 해 => 매직 메소드라고 함

- 객체의 특수 조작 행위를 지정 (함수, 연산자 등)

  - `_ _str_ _` : 해당 객체의 출력 형태를 지정
    - 프린트 함수를 호출할 때 자동으로 호출
    - 어떤 인스턴스를 출력하면 `_ _ str_ _` 의 return 값이 출력


```python
class Person():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'나는 {self.name}'
p1 = Person('miae')
print(p1) # => 나는 miae
```

- `_ _gt_ _`: 부등호 연산자 (greater than)



### 클래스

### 메소드



## 객체지향의 핵심개념

### 추상화

### 상속

### 다형성

