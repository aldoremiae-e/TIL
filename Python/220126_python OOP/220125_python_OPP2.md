



## 객체지향의 핵심개념

### 추상화

- 세부적인 내용을 감추고 필수적인 부분만 표현하는 것을 뜻한다.
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용

### 상속

> 상속이란 두 클래스 사이 부모-자식 클래스를 성립

- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아진다.

```python
class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
class Student(Person):
    def __init__(self, student_id, name='학생'):
        self.name = name
        self.student_id = student_id  
        Person.population += 1
    
s1 = Student(1,'김학생')
print(s1.name, s1.student_id) # => 김학생 1
# 자식 클래스의 인스턴스는 부모 클래스의 메서드를 호출 할 수 있음
s1. talk() # => 반갑습니다. 김학생입니다.
```

- `issubclass(class, classinfo)`

  - classinfo : 부모클래스, class : classinfo 의 자식클래스일 때 True

    ```python
    issubclass(Student, Person) # => True
    ```

    

- `isinstance(object, classinfo`)

  - object가 classinfo의 인스턴스 또는 classinfo의 자식클래스일 경우 True 

    ```python
    print(isinstance(s1,Student), isinstance(s1,Person)) # => True True
    ```



```python
#bool 자료형은 int 자료형의 자식클래스임
print(issubclass(bool, int)) # True
#float 자료형은 int 자료형의 자식클래스 아님
print(issubclass(float, int)) # False
```



- 만약 자식 클래스의 초기화(생성자 메서드)에서 부모 클래스와 중복이 발생한다면

  - `super()` 함수를 통해 중복을 제거

  ```python
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email
      
      def greeting(self):
          print(f'안녕 {self.name}')
  
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          # Person 클래스
          super().__init__(name, age, number, email)
          self.student_id = student_id
  ```

  

### 다형성

> 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음

- 서로 다른 클래스에 속해있는 객체들이 동일한 메세지에 대해 각기 다른 방식으로 응답할 수 있다.

> 메서드 오버라이딩 

- 자식 클래스에서 부모 클래스의 메서드를 `재정의`하는 것

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def talk(self):
        print(f'안녕, {self.name}')
        
# 위의 Person 클래스를 상속 받아 군인답게 말하는 Soldier 클래스를 만들어봅시다.
# talk 메서드를 재정의(override)합니다.

class Soldier(Person):
    def __init__(self, name, age, number, email, army):
        super().__init__(name, age, number, email)
        self.army = army
        
    def talk(self):
        print(f'충성! {self.army} {self.name}')
```



### 캡슐화

> 객체의 일부 구현에 대해 외부의 직접적인 엑세스를 차단해줌

- Public Member - 어디서나 호출가능

- Protected Member - 언더바 1개로 시작

  - 암묵적 규칙에 의해 부모 클래스 내부, 자식 클래스에서만 호출

  ```python
  class Person:
      
      def __init__(self,name,age):
          self.name = name
          self._age = age
          
      def get_age(self):
          return self._age
      
  p1 = Person('김미애',26)
  p1.get_age() # => 26
  p1._age # => 26
  ```

- Private Member - 언더바 2개로 시작

  - 본 클래스 내부에서만 사용, 하위 클래스 상속 및 호출 불가, 외부 호출 불가

  ```python
  class Person:
      
      def __init__(self, name, age):
          self.name = name
          self.__age = age
      
      def get_age(self): 
          return self.__age
  
  p1 = Person('김미애', 26)
  p1.get_age() # => 26
  p1.__age # => AttributeError : 직접 접근 불가
  
  ```

- **`getter`** 메서드와 **`setter`** 메서드 

  - `getter` : 변수의 값을 읽는 메서드
  - `setter` : 변수의 값을 설정하는 성격의 메서드



### 다중상속

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):
    gene = 'XX'    
    def swim(self):
        return '엄마가 수영'
    
class Dad(Person):
    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'
    
class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'
```

```python
baby1 = FirstChild('아가') 
baby1.cry()		# =>'첫째가 응애'
baby1.swim()	# =>'첫째가 수영'
baby1.walk()	# => '아빠가 걷기' 부모클래스에서 가져옴
baby1.gene		# =>'XY' 첫번째 부모클래스 변수를 반환
```



### 상속관계에서의 이름 공간과 MRO (Method Resolution Order)

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.
  - 인스턴스 -> 자식 클래스 -> 부모 클래스
- MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드입니다.

```python
print(FirstChild.__mro__)
# => (<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>)
```

