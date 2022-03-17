# 0314 Database



## DB

> 데이터베이스는 체계화된 데이터의 모임

- 몇개의 자료 파일을 조직적으로 구조화 시켜서 기억시켜 놓는 자료의 집합체

- 장점 : 중복 최소화, 데이터 무결성(정확한 정보를 보장), 데이터 보안 유지 등



### RDB (관계형 데이터베이스)

> 키와 값들의 간단한 관계를 표의 형태로 정리한 데이터베이스

- 스키마 (schema) : 무결성을 위해 어떠한 필드를 타입으로 지정해놔서 , 데이터베이스의 자료의 구조 등 전반적인 명세를 기술한 것
- 테이블 (table) : 열(컬럼/필드)과 행(레코드/값)이 모델을 사용해 조직된 데이터 요소들의 집합
- 기본키 (Primary Key) : 각 행의 고유 값



### RDBMS (관계형 데이터베이스 관리 시스템)

ex) SQLite Mysql 등등

- Djando => DB관리 : model을 이용해서 관리

  - model의 클래스에서 필드 타입 등을 정의 (스키마 역할)
  -  -> 마이그레이션 파일 생성 : 
    - 마이그레이션 파일에서는 무슨 일을 하느냐?
      - 모델에서 클래스를 바꾸면 migration 파일을 만들면서 기존 것과 변경해서 어떤식으로 변경할지를 알아서 만들어줘서 DB 반영 전의 중간단계라고 볼 수 있다.
  - -> 마이그레이트를 통해 DB 직접 반영

  

#### SQLite

> 장고에서 쓰이는 비교적 가벼운 데이터베이스

1. Type Affinity 

   - 권장되는 데이터의 선호도를 맞춰서 작성하는 것이 좋음

   1. INTEGER
   2. TEXT
   3. BLOB
   4. REAL
   5. NEMERIC



## SQL

> RDBMS의 데이터 관리를 위해 특수 목적으로 설계된 프로그래밍 언어



#### 분류

1. DDL : 데이터 정의 언어 : 테이블, 스키마 를 정의하기 위한 명령어
2. DML : 데이터 조작 언어 : 데이터를 저장,조회,수정,삭제 등 조작 명령어
   - INSERT, SELECT, UPDATE, DELETE
3. DCL : 데이터 제어 언어



### DML

#### CREATE

- 모델 -> 마이그레이션 파일을 생성 -> 마이그레이트
- 모델을 만들면 

- INSERT : 테이블에 행(레코드)를 삽입



> 데이터베이스 생성하기

1. csv 파일을 table로 만들기

```bash
$ sqlite3 tutorial.sqlite3
SQLite version 3.38.1 2022-03-12 13:37:29
Enter ".help" for usage hints.
sqlite> .database
main: C:\Users\bamxd\Desktop\SQL\SQL\tutorial.sqlite3 r/w
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> .tables
examples
```



### SQL Qurey 문

> SELECT 

- 특정 테이블의 레코드(행) 정보를 반환해주는 역할

```bash
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
```

```bash
# 헤더까지
sqlite> .headers on
sqlite> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000
```

```bash
# 행분리
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-0000-0000
```



> CREATE 테이블 생성 -> 우클릭 -> RUN QUERY

```sql
-- SQLite
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
  age INT
  address TEXT
);
```

```sqlite
sqlite> .schema classmates --테이블조회
---------------------------
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
  age INT
  address TEXT
);
```

> 테이블 삭제

```sqlite
sqlite> DROP TABLE classmates;
```



### CRUD

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |



## 조회

### WHERE

### Aggregate Functions

> 집계 함수

#### 1. COUNT

#### 2. AVG

#### 3. MAX

#### 4. MIN

#### 5. SUM



### LIKE

> 패턴 일치를 기반으로 데이터를 조회하는 방법

#### 와일드 카드

- 1. `%` : 0개 이상의 문자

- 2. `_` : 임의의 단일 문자



### ORDER BY

> 조회 결과 집합을 정렬

- SELECT 문에 추가하여 사용
- 정렬순서 : 오름차순 `ASC`  (default), 내림차순 `DESC`



### GROUP BY

> 행 집합에서 요약 행 집합을 만듦

- SELECT문의 option절
- 문장에 WHERE 문이 포함된 경우 WHERE문 뒤에 작성



### ALTER TABLE

- 기능

  1. 테이블 이름 변경

  2. 테이블에 새로운 컬럼 추가

  3. 새로운 컬럼 추가

  - 조건에 NOT NULL 에 넣었더니 에러가 뜸 - 값 내용이 자체가 없는데 (NULL이 아닌데) 뭔 NOT NULL이냐!
    - 해결 방법1 : NOT NULL 설정 없이 추가하기
    - 해결 방법2 : 기본 값 (DEFAULT) 설정하기

  4. Drop column  삭제 (ver 3.35)





## SQL vs Django-ORM

차이가 뭔지 알아보자

| 조회         |                      SQL                       |                 ORM                  |
| ------------ | :--------------------------------------------: | :----------------------------------: |
| 모두검색     |        SELECT * FROM articles_article;         |        Article.objects.all()         |
| *(확인방법)* |                                                |    *Article.objects.all().query*     |
| 특정검색     | SELECT * FROM articles_article WHERE rowid=1;  |      Article.objects.get(pk=1)       |
| *(확인방법)* |                                                | *Article.objects.filter(pk=1).query* |
| 삭제         | DELETE FROM articles_article <br/> WHERE id=1; |  Article.objects.get(pk=1).delete()  |
|              |                                                |                                      |
|              |                                                |                                      |
|              |                                                |                                      |
|              |                                                |                                      |

