# DB총정리

## 목차

### 1. Database

- RDB
- RDBMS

### 2. SQL

- 테이블 생성 및 삭제
- CRUD
- WHERE
- Aggregate Functions
- LIKE
- ORDER BY / GROUP BY
- ALTER TABLE

### 3. Model Relationship1

- Foreign Key
- Customizing authentication in Django

### 4. Model Relationship2

- User - Article
- User - Comment

<hr>

## 1. Database

> 데이터베이스는 체계화된 데이터의 모임

- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료를 구조화 함으로서 검색과 갱신의 효율화
- 여러 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고, 자료를 구조화하여 기억시켜 놓은 자료의 집합체



DB의 장점

- 데이터 중복 최소화
- 데이터 무결성
- 데이터 일관성
- 데이터 독립성
- 데이터 표준화
- 데이터 보안 유지



### RDB (Relational Database)

> 관계형 데이터베이스
>
> 키(key)와 값(value)들의 관계를 표로 정리한 데이터베이스

- 스키마 (schema) : DB에서의 자료의 명세를 나타내줌 (자료 구조, 표현방법, 관계)

  | column  | datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | address | TEXT     |

  

- table : 열과 행의 모델을 사용해 조직된 데이터 요소들
  - 열 = 컬럼 = 필드 : 고유한 데이터 형식이 지정됨
  - 행 = 레코드 = 값 : 실제 데이터가 저장되는 형태
  - PK (기본키) : 각 행의 고유 값, 반드시 설정해야하고, DB관리 및 관계 설정 시 주요하게 활용

| id   | name   | address |
| ---- | ------ | ------- |
| 1    | 홍길동 | 제주    |
| 2    | 김길동 | 서울    |
| 3    | 박길동 | 독도    |



### RDBMS (Relational Datebase Management System)

> 관계형 데이터베이스 관리 시스템

ex ) MySQL , SQLite, PostgreSQL, ORACLE, MS SQL 등

- SQLite : 비교적 가벼운 데이터베이스 관리 시스템 - 파일 형식으로 응용 프로그램에 넣어서 사용된다. 

  ```
  1. NULL
  2. INTEGET : 크기에 따라 0,1,2,3,4,6 또는 8바이트에 저장된 부호 있는 정수
  3. REAL : 8바이트 부동소수점 값
  4. TEXT
  5. BLOB : 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)
  ```

  - SQLlite Type Affinity : 특정 컬럼에 저장하도록 권장하는 데이터 타입

    ```
    정수같은거 : INTEGER
    글같은거 :TEXT
    별다른거 없는거 : BLOB
    소수점있는거 : REAL
    날짜시간같은거 : NUMERIC
    ```

<hr>

## 2. SQL (Structured Query Language)

> 관계형 데이터베이스 관리시스템 (RDBMS) 의 데이터 관리를 위해 설계된 프로그래밍 언어

- 정의 : DB스키마 생성 및 수정
  - `DDL - 데이터 정의 언어` :  RDB를 정의하기 위한 명령어
    - ex ) CREATE, DROP, ALTER
- 조작 : 자료의 검색 및 관리
  - `DML - 데이터 조작 언어` : 데이터를 CRUD 하기 위한 명령어
    - ex ) INSERT, SELECT, UPDATE, DELETE
- 제어 : DB객체 접근 조정 관리
  - `DCL - 데이터 제어 언어` : DB사용자의 권한 제어를 위해 사용하는 명령어
    - ex ) GRANT, REVOKE, COMMIT, ROLLBACK



### 테이블 생성 및 삭제

1. DB생성

   ```bash
   sqlite3 tutorial.sqlite3
   .database	# 데이터베이스 이름 = tutorial.sqlite3
   ```

2. csv파일 table로 만들기

   ```bash
   .mode csv
   .import csv이름.csv 테이블이름
   .tables # 테이블 조회
   ```

3. SELECT

   ```bash
   SELECT * FROM 테이블이름;
   
   1,"길동","홍",600,"충청도",010-0000-0000
   ```

   - ; 까지 하나의 명령(SQLQuery) 로 간주 된다
   - SELECT 문은 특정 테이블의 레코드(행) 정보를 반환

- 터미널 view 변경하기 (어떻게 보이는지)

  ```bash
  .headers on
  SELECT * FROM 테이블이름;
  
  1,"길동","홍",600,"충청도",010-0000-0000
  ```

  ```bash
  .mode column
  SELECT * FROM 테이블이름;
  
  d  first_name  last_name  age  country  phone
  --  ----------  ---------  ---  -------  -------------
  1   길동          홍          600  충청도      010-0000-0000
  ```

  

*SQLite 확장프로그램 사용*

> 우클릭 Open Datebase => SQLITE EXPLORE 우클릭 - NewQuery = > 코드 작성 후 우클릭 => Run Query(ctr+shift+Q)



- CREATE TABLE : DB에 테이블 생성

```sqlite
''' SQLite '''
-- SQLite
CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT
);
```

```bash
# 특정 테이블의 스키마 조회
.schema classmates

CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT
);
```



- DROP TABLE : DB에 테이블 제거

```bash
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```

<hr>

### CRUD

|      | 구문   | SQL                                                          | ORM                                                          |
| ---- | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| C    | INSERT | INSERT INTO 테이블이름 (컬럼1, 컬럼2, ..) VALUES (값1, 값2,..); <br>컬럼값이 모두 있을 떄는 굳이 써주지 않아도 됨 <br>rowid 쓸거면 쓰게 되어있음 | Artciel.objects.create(필드1='값1', 필드2='값2',..)<hr><br />article = Article()<br>article.title='제목'<br>article.content='내용'<br>article.save()<br>artocle = Article(title='제목', content='내용') |
| R    | SELECT | 전체 조회 : SELECT * FROM 테이블이름;<br>개별 조회1 : SELECT 컬럼1, 컬럼2, .. FROM 테이블이름;<br>개별 조회2 : SELECT 컬럼1, 컬럼2, .. FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;<br>조건 조회 : SELECT 컬럼1, 컬럼2, .. FROM 테이블이름 WHERE 조건; | 전체 조회 : Article.objects.all()<br>조건 조회: Article.objects.get(pk=pk)<br />필드 조회: Article.objects.filter(조건).value(필드)<br /><br /> 개별조회2: Article.objects.order_by(-age)[:숫자]<br />필터 이용 조건조회 : Atricle.objects.filter(조건).value('필드') |
| U    | UPDATE | UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, .. WHERE 조건;   | article = Article.objects.get(pk=101)<br />article.last_name='김'<br />article.save() |
| D    | DELETE | DELETE FROM 테이블이름 WHERE 조건;                           | Article.objects.get(pk=101).delete()                         |



#### CRUD - CREATE

> 테이블에 단일 행 삽입

```sqlite
INSERT INTO classmates (name, age) VALUES ("홍길동", 23);
INSERT INTO classmates (name, age, address) VALUES ("홍길동", 30. "서울");
INSERT INTO classmates VALUES ("홍길동동", 30, "서울");
```

```bash
SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
홍길동  30   서울
홍길동동  30   서울
```

![image-20220417191138632](DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220417191138632.png)



- PK(id)를 따로 작성하지 않았다 :

  SQLite에서 PK 속성의 컬럼 값이 자동으로 증가하는 PK옵션을 가진 rowid를 정의한다

  ```bash
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   23
  2      홍길동   30   서울
  3      홍길동동  30   서울
  ```

  

- address  에 NULL 존재 : 만약 꼭 필요한 정보라면 공백으로 비워두면 안된다 - NOT NULL설정

  => 지우고 새로 만들어야한다.

  ```sqlite
  -- SQLite
  CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
  );
  
  -- INSERT INTO classmates VALUES ("홍길동", 30, "서울");
  
  -- 에러 : Parse error near line 11: table classmates has 4 columns but 3 values were supplied 
  
  INSERT INTO classmates VALUES (1, "홍길동", 30, "서울");
  ```

  

#### CRUD - READ

> SELECT :테이블에서 데이터를 조회

- SELECT 문은 다양한 절(clause)와 함께 쓰인다

  - `LIMIT` : 쿼리에서 반환되는 행 수를 **제한**

    - 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용

    ```bash
    # id, name 컬럼 값을 세번째에 있는 하나만 조회
    # OFFSET 숫자는 0부터 시작하고, 포함되지 않는다.
    sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
    
    rowid  name
    -----  ----
    3      이싸피
    ```

    

  - `WHERE` : 쿼리에서 반환된 행에 대한 특정 검색 **조건**을 지정

    ```bash
    # id, name 컬럼 값을 주소가 서울인 데이터만 가져오시오
    sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
    rowid  name
    -----  ----
    1      홍길동
    ```

    

  - `SELECT DISTINCT` : 조회 결과에서 **중복 행을 제거**

    - SELECT 키워드 바로 뒤에 작성해야한다.

    ```bash
    #  age 컴럼 값을 중복 없이 가져오시오 (30 중복됨)
    sqlite> SELECT DISTINCT age FROM classmates;
    age
    ---
    30
    26
    29
    28
    ```

    

#### CRUD - DELETE

> 테이블에서 행을 제거

- 조건에 맞는 데이터를 삭제할 때 : 

  ```bash
  sqlite> DELETE FROM classmates WHERE rowid=5;
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   30   서울
  2      김철수   30   대전
  3      이싸피   26   광주
  4      박삼성   29   구미
  ```

  - 기본적으로 SQLite는 id를 재사용한다. => 다시 INSERT하면 rowid 5로 나옴.



- id를 재사용하지 않기 위해서 : 테이블을 생성하는 단계에서 `AUTOINCREMENT` 을 작성하여 설정 가능 



#### CRUD - UPDATE

> 기존 행의 데이터를 수정

- `SET` clause에서 테이블의 각 열에 대해 새로운 값을 설정

```bash
sqlite> UPDATE classmates SET name='홍길동', address='제주도' where rowid=5;
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   30   대전
3      이싸피   26   광주
4      박삼성   29   구미
5      홍길동   28   제주도
```



<hr>

### WHERE

- ```bash
  SELECT 컬럼1, 컬럼2 FROM 테이블이름 WHERE 조건 AND/OR 조건;
  ```

  

### Aggregate funticon (집계함수)

> 값 집합에 대한 계산을 수행하고 단일 값을 반환

- 여러 행으로부터 하나의 결과값을 반환하는 함수로, `SELECT 구문에서만` 사용

  *기본적으로 아래 함수들은 컬럼 데이터타입이 숫자일 때만 사용가능*

  - `COUNT(*)` : 테이블 전체 행 수를 구하는 함수
  - `AVG(age) `: age 컬럼 전체 평균 값을 구하는 함수
  - `MAX`, `MIN`, `SUM`

  ```bash
  SELECET 컬럼1, 집계함수(숫자컬럼) FROM 테이블이름 WHERE 조건;
  ```

  ```python
  #ORM - count
  Article.objects.filter(조건1, 조건2).count() #AND
  Article.objects.filter(Q(조건1)|Q(조건2)).count() #OR
  len(Article.objecnts.all())
  ```
  
  

### LIKE

> 패턴 일치를 기반으로 데이터를 조회하는 방법

*와일드카드 : 파일을 지정할 때 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 문자*

- 와일드카드 : SQLite 에서 패턴 구성을 위해 2개의 와일드카드 제공
  - `%` : 0개 이상의 문자 - 이 자리에 문자열이 있을수도, 없을수도 있다
  - `_` : 임의의 단일문자 - 반드시 이 자리의 한 개의 문자가 존재해야 한다.

​	

Q ) 나이가 20대인 사람만 조회한다면

```bash
# 2로 시작하고 _ 총 2자리인 값
SELECT * FROM users WHERE age LIKE '2_';

# 2로 시작하는 값 : 근데 이거는 2살이랑 200살도 되서 안됨
# SELECT * FROM users WHERE age LIKE '2%'; 
```

Q ) 지역번호가 02인 사람만 조회한다면

```bash
# 02- 로 시작하는 값
sqlite> SELECT rowid, * FROM users WHERE phone LIKE '02-%';

# 02로 시작하는 값 : 023, 0222 같은 값이 있으면 이것도 같이 조회되서 - 필요함
sqlite> SELECT rowid, * FROM users WHERE phone LIKE '02%';
```

Q) 이름이 '준'으로 끝나는 사람만 조회한다면

```bash
# 준으로 끝나는 값
sqlite> SELECT rowid, * FROM users WHERE first_name LIKE '%준';
# 2글자인데 준으로 끝나는 말 : 그럼 최준은 조회안됨
sqlite> SELECT rowid, * FROM users WHERE first_name LIKE '_%준';
```

Q ) 중간번호가 5114인 사람만 조회한다면

```bash
sqlite> SELECT rowid, * FROM users WHERE phone LIKE '%-5114-%';
```



### ORDER BY (정렬)

> 조회 결과 집합을 정렬

- SELECT문에 추가하여 사용
- 정렬 순서를 위한 2개의 키워드 제공
  - ASC : 오름차순(Default)
  - DESC : 내림차순

```bash
SELECT * FROM 테이블이름 ORDER BY 컬럼1, 컬럼2, .. ASC/DESC LIMIT 숫자 OFFSET 숫자;
```



### GROUP BY (요약)

> 데이터 요약

- SELECT 문의 optional 절
- 문장에 WHERE 절이 포함된 경우 반드시 **WHERE 뒤에 작성**

```bash
SELECT 컬럼1, Aggregate_function(컬럼2) FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
```



Q ) 각 성씨가 몇 명씩 있는지 조회한다면

```bash
sqlite> SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
last_name  COUNT(*)
--------- ---------

# COUNT(*)에 해당하는 컬럼명을 바꿔서 조회 : AS 이용
sqlite> SELECT last_name, COUNT(*) AS count_name FROM users GROUP BY last_name;
last_name  count_name
---------  ---------
```



### ALTER TABEL (테이블 수정)

- 테이블 이름 수정

  ```	bash
  sqlite > ALTER TABLE articles RENAME TO news;
  ```

  

```bash
sqlite> ALTER TABLE news ADD COLUMN create_at TEXT NOT NULL;

# Runtime error: Cannot add a NOT NULL column with default value NULL
```

```
NOT NULL을 안써버리거나, DEFAULT '어쩌구'; 를 해놔버린다.
```



<hr>

## 3. Model Relationship

### Foreign Key 

> 외래키 : RDB에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키

- 참조하는 테이블에서 속성(필드)에 해당하고, 참조되는 테이블에서 기본 키(PK)를 가리킨다.

  - 참조하는 테이블의 외래 키는 참조되는 테이블 행 1개에 대응

  - 참조하는 테이블의 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음

    <img src="DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220418035248728.png" alt="image-20220418035248728" style="zoom:50%;" />

-  키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
  - 외래 키의 값이 부모 테이블의 PK일 필요는 없지만, 고유성이 있어야 함.



###  ForeignKey field (1:N)

- 2개의 위치 인자가 반드시 필요

  1. 참조하는 model class

  2. on_delete 옵션
     - 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 것인가?
     - 데이터 무결성을 위해서 매우 중요한 설정임!!
     - on_delete=models.CASCADE : 부모객체가 삭제되었을 때 이를 참조하는 객체도 삭제

- migration 할 때 필드 이름에 _id 를 추가하여 DB 열 이름 추가

```python
# models.py
class Comment(models.Model):
    article = models.ForiegnKey(Article, on_delete=models.CASCADE)
```

- ForeignKey 인스턴스 생성 : comment DB에 article DB를 부모로 하는 외래키 생성
  - 클래스 이름의 소문자로 생성하는게 기본

![image-20220418040617378](DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220418040617378.png)



### 댓글 생성

- 에러 `IntegrityError: NOT NULL constraint failed: articles_comment.article_id`

  => article에 데이터가 없기 때문임 => article에 게시글 생성

- 역참조(1=>N) : article 즉 부모 인스턴스 입장에서 참조하고 있는 자식 조회 (댓글 조회)

  ```shell
  # 댓글 조회
  article.comment_set.all()
  
  # 조회한 모든 댓글 출력하기
  comments = article.comment_set.all()
  for comment in comments:
  	print(comment.content)
  ```

- 참조 (N => 1) : comment 에서 자신이 참조하고 있는 게시글을 접근 조회

  ```shell
  # 게시글 조회
  comment.article.all()
  
  # 개별 게시글 조회
  comment = Comment.objects.get(pk=1)
  # 제목
  comment.article
  # 내용
  comment.article.content
  # 외래키
  comment.article_id
  ```



- detail 페이지에서 CommentForm 생성

  ```python
  # forms.py
  class CommentForm(forms.ModleForm):
      class Meta:
          model = Comment
          exclude = ('article',) # 외래키 제외, 튜플로 해야함
  ```

  - 외래키필드를 작성자가 입력하는 상황을 없애기 위해 외래키 제외

  ```python
  # articles/view.py
  
  def comments_create(request, pk):
      # 게시글 정보가져와
      article = get_object_or_404(Article, pk=pk)
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.article = article
          comment.save()
      return redirect('articles:detial',article.pk)
  ```

  `comment = comment_form.save(commit=False)` : 아직 데이터베이스에 저장되지 않은 인스턴스를 반환한것

### Customizing authentication in Django

> 회원가입 커스텀

- User 모델 대체하기
  - Django 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있기 때문
  - User을 참조하는데 사용하는 **`AUTH_USER_MODEL`**값을 제공하여, user라는 기본 모델을 재정의할 수 있도록 한다.

1. AbstractUser : 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본 클래스

   - AbstractUser을 상속받아서 새로운 User 모델 작성

   ```python
   # accounts/models.py
   
   from django.contrib.auth.models import AbstactUser
   
   class User(AbstractUser):
       pass
   ```

2. 기존 Django 의 User 모델이었던 auth 앱의 User모델 안쓰고 내 User을 쓰기 위해 변경

   ```python
   # settings.py
   
   AUTH_USER_MODEL = 'acounts.User'
   ```

3. admin site 에 Custom User 모델 등록

   ```python
   # accounts/admin.py
   
   from django.contrib.auth.admin import UserAdmin
   from .models import User
   
   admin.site.register(User, UserAdmin)
   ```

4. migration



- 회원가입 시 에러

  ![image-20220418043403950](DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220418043403950.png)

  - forms.py에서 폼을 확장해야한다.

  ```python
  # forms.py
  
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm
  from django.contrib.auth import get_user_model
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta):
          model = get_user_model() #User
          fields = UserCreationForm.Meta.fields + ('email같은거',)
  ```

  - `get_user_model()` : 현재 프로젝트에서 활성화된 사용자 모델을 반환 



<hr>



## 4. Model Relationship2

### User - Article (1:N)

- settings.AUTH_USER_MODEL

  - User 모델에 대한 외래 키 나 N:N 관계를 정의할 때 사용

  - models.py에서 User 모델 참조할 때 사용

- get_user_model()

  - 현재 프로젝트에서 활성화된 User 모델을 반환
    - 커스텀한 User 모델이 있는 경우 그 모델을 반환하고, 아니면 그냥 User 모델 반환
  - models.py 아닌 다른 모든 곳에서 User 모델을 참조할 떄 사용

```python
# articles.models.py
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

 =>  마이그레이션 해줌

- 에러 

  ![image-20220418044809303](DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220418044809303.png)

  에러 해결 : 게시글 작성 시 작성자 정보(article.user)가 누락되었기 때문에 추가 후 게시글 작성

  ```python
  # articles/views.py
  
  def create(request):
      if request.method = 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():
              # 아직 폼에 저장되지 않은 DB를 인스턴스로 반환 후 저장
              article = form.save(commit=False)
              # 누락된 작성자 정보를 요청받아서 가져옴
              article.user = request.user
              article.save()
              return redirect('articles:detail', article.pk)
  ```

  

### User - Comment

- 에러

  ![image-20220418045907116](DB%EC%B4%9D%EC%A0%95%EB%A6%AC.assets/image-20220418045907116.png)

  - 댓글 작성 시 작성자 정보가 누락되었기 때문에 추가해 주어야함

  ```python
  # articles.views.py
  
  def comment_create(request,pk):
      # 회원인지
      if request.user.is_authenticated:
          # 게시글과 요청받은 댓글 폼 가져오기
          article = get_object_or_404(Article, pk=pk)
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.article = article
              comment.user = request.user
              comment.save()
              return redirect('articles:detail', article.pk)
      return redirect('accounts:login')
  
  ```

  