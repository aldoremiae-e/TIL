# 0308 Model

## 흐름 그림

> 오늘의 목표 게시판 만들기!!

<img src="0308%20Model.assets/image-20220308124322056.png" alt="image-20220308124322056" style="zoom:50%;" />



## Model 개념

> 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구



- Django는 model을 통해 DB에 접속하고 관리를 한다.
- 각각의 model은 하나의 DB 테이블에 매핑 되어있다.
- 즉 model은 데이터에 대한 정보를 가지고 있고, 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함한다.

**DB : 체계화된 데이터의 모임**

- 스키마 : DB에서 자료의 구조, 표현방법, 관계 등을 정의한 구조
- 테이블 : 열(컬럼,필드,데이터형식) 행(레코드, 튜플, 데이터값)
- PK : 각 행의 고유값, 반드시 설정하여야하고 데이터베이스 관리 및 설정에 주요하다.

**쿼리 : 데이터를 조작하기 위한 명령어**

**SQL : 구조화시킨 쿼리를 조작하기 위한 언어**



## Migration

| models.py | class에 필드값 생성,수정        |
| --------- | ------------------------------- |
| migration | python manage.py makemigrations |
| migrate   | python manage.py migrate        |



### 1. models. py

> Model - Class 만들기 혹은 변경시 - 속성: 필드(타입)
>
> ```python
> from turtle import update
> from django.db import models
> 
> # Create your models here.
> # models.Model을 상속 받아서 만든다.
> class Article(models.Model):
>     # Class 속성 : 데이터베이스의 필드(컬럼)
>     title = models.CharField(max_length=30)
>     content = models.TextField()
>     # 처음 추가할 때만 저장
>     created_at = models.DateTimeField(auto_now_add=True)
>     # 뭔가 변경될 때마다 저장
>     update_at = models.DateTimeField(auto_now=True)
> 
> # 변수의 이름을 짓는 패턴
> # CamelCase => Class
> # snake_case=> function, variable
> ```
>
> 

<img src="0308%20Model.assets/image-20220308125953181.png" alt="image-20220308125953181" style="zoom:50%;" />



### 2. $ python manage.py makemigrations

> Makemigragions : 마이그레이션(설계도) 파일 생성
>
> models.py 저장 후 migration 시작

```bash
$  python manage.py makemigrations
```



*참고 SQLite 설치* 

<img src="0308%20Model.assets/image-20220308130915837.png" alt="image-20220308130915837" style="zoom:50%;" />



### 3. $ python manage.py migrate

> migrate : 실제로 DB를 반영하는 작업

```bash
$  python manage.py migrate
```



### 4. 확인

> pk 값은 자동적으로id 값으로 부여가 되는 것 같다.

<img src="0308%20Model.assets/image-20220308130952518.png" alt="image-20220308130952518" style="zoom: 50%;" />



### # created_at, updated_at (시간) migration 하기

- models.py

  ```python
  # 처음 추가할 때만 저장
    created_at = models.DateTimeField(auto_now_add=True)
  # 뭔가 변경될 때마다 저장
    update_at = models.DateTimeField(auto_now=True)
    
  ```

  

- $ python manage.py makemigrations  (쓰고 1. enter, enter)

  > migration 파일 생성

  ```bash
   $ python manage.py makemigrations
   # 새로운 필드가 추가되었는데 기본 값이 없다.
   # 왜 문제된다? DB에 값이 필수로 설정되어 있어서. 빈 값은 존재할 수 없도록 되어 있어서.
  You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
  # 옵션 
  # 1. 내가 지금 직접 디폴트값을 줄게 => 
  # 2. 미안. 나 종료하고 models.py에서 내가 직접 설정할게 
  1) Provide a one-off default now (will be set on all existing rows) 
  2) Quit, and let me add a default in models.pySelect an option: 1    
  # 디폴트 값을 파이썬 문법으로 유효한 것을 입력해.
  Please enter the default value now, as valid Python
  # 너 이거 DateTime인데.... 2022-03-08 13:17 직접 X 파이썬 코드로 할 수 있도록 도와줌
  # 엔터만 누르면 지금 너 timezone에 맞는 현재시간으로 해줄게
  You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
  The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now  
  Type 'exit' to exit this prompt[default: timezone.now] >>>
  Migrations for 'articles':  
  articles\migrations\0002_auto_20220308_1314.py    
  - Add field created_at to article    
  - Add field updated_at to article
  ```

  

- $ python manage.py migrate

  >  DB반영
  
  ```bash
  $ python manage.py migrate
  ```



- 결과

<img src="0308%20Model.assets/image-20220308132807992.png" alt="image-20220308132807992" style="zoom:50%;" />



## ORM -Query

> ORM : Object Relational Mapping : 객체-관계 매핑
>
> 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해어, 객체를 통해 간접적으로 데이터베이스의 데이터를 다룬다.
>
> 객체 - 객체 지향 프로그래밍은 **Class**를 사용
>
> 관계형 데이터베이스 - **테이블**을 사용

- DB를 객체로 조작하기 위해 ORM을 사용한다.

- OOP 프로그래밍(Python)에서 관계형 데이터베이스 관리 시스템(SQLite)을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않은 데이터를 변환한다. 

  | 장점                                                         | 단점                                      |
  | ------------------------------------------------------------ | ----------------------------------------- |
  | SQL을 알지 못해도 DB 조작이 가능 <br>객체지향적 접근으로 생산성을 높일 수 있음 - 현대 웹 프레임워크의 요점은 생산성을 높이는 데 있기 때문에 큰 장점임 | ORM만으로 완전한 서비스를 구현하기 어려움 |

  

1. 장고 익스텐션 설치 및 앱 등록 , 실행

```bash
miae@DESKTOP-TSJ4J9N MINGW64 ~/Desktop/Django_0308
$ pip install ipython django-extensions
```

![image-20220308135033427](0308%20Model.assets/image-20220308135033427.png)

> _로 저장하는 것 주의

```bash
$ python manage.py shell_plus
```



## DB API

> DB를 조작하기 위한 도구

Model을 만들면 Django는 객체를 CRUD 할 수 있는 database-abstract API (database-access API)를 자동으로 만듬

```bash
#클래스이름.Manager.QuerySet API
Article.objects.all
```

- 클래스이름 : models.py에 생성한 클래스 이름
- Manager : Django 모델에 DB 쿼리 작업이 제공되는 인터페이스
- QuerySet : 데이터베이스로부터 전달받은 객체 목록
  - QuerySet 안에 객체는 0개, 1개 혹은 여러개 일 수 있다
  - DB로부터 조회, 필터, 정렬 등을 수행할 수 있다.



### CREATE

```powershell
# 조회했을 때 아직 쿼리셋에 아무 것도 없음
In [3]: Article.objects.all()
Out[3]: <QuerySet []>
# Article 클래스로부터 article 인스턴스 생성
In [4]: article = Article()
# 값 할당 1번 방법
article.title = 'first'
article.content = 'django'

# 아직 DB에 저장되어있지 않음
In [5]: article
Out[5]: <Article: >

In [6]: Article.objects.all()
Out[6]: <QuerySet []>

# 인스턴스를 DB에 저장
aritcle.save()

In [13]: Article.objects.all()
Out[13]: <QuerySet [<Article: first>]>
In [14]: article
Out[14]: <Article: first>
```

```powershell
# 인스턴스에 할당방법 2번째
In [17]: article = Article(title='second', content='django')

In [18]: Article.objects.all()
Out[18]: <QuerySet [<Article: first>]>
# 인스턴스변수는 변했기 때문에 second
In [19]: article
Out[19]: <Article: second>

In [20]: article.save()

In [21]: article
Out[21]: <Article: second>
# DB에 저장된거 반영한 조회
In [22]: Article.objects.all()
Out[22]: <QuerySet [<Article: first>, <Article: second>]>

```

```shell
# QuerySetAPI -create() 사용해서 할당 3번째

In [25]: Article.objects.create(title='third', content='django')
Out[25]: <Article: third>

In [26]: Article.objects.all()
Out[26]: <QuerySet [<Article: first>, <Article: second>, <Article: third>]>
# 인스턴스 변수는 그대로 second
In [27]: article
Out[27]: <Article: second>
```

```python
#model.py

def __str__(self):
    return self.title
```

- 표준 파이썬 클래스의 메소드인 str()을 정의하여, 각각의 객체가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음. 작성후 shell_plus 재시작해야함.



### READ

#### all()

> 해당 클래스(테이블) 데이터 조회 => QuerySet (객체들로 구성된)

```shell
Article.objects.all()
```



#### get() 

>  단일데이터 조회 => 고유성이 있는 객체로만 접근이 가능하다
>
>  에러 상황 : 1. 데이터 결과가 없을 때	2. 데이터 결과가 중복되었을 때

```python

In [29]: Article.objects.get(pk=1)
Out[29]: <Article: first>

In [30]: Article.objects.get(pk=100)
# DoesNotExist: Article matching query does not exist.

In [31]: Article.objects.get(content='django')
# MultipleObjectsReturned: get() returned more than one Article -- it returned 3!    
```



#### filter()

> 여러데이터 조회 = > Out : Queryset (리스트같은애) 이라는 객체로 접근 가능

```python
In [32]: Article.objects.filter(content='django')
Out[32]: <QuerySet [<Article: first>, <Article: second>, <Article: third>]>
```



### UPDATE

```python
# 인스턴스에 접근하여서 수정가능
In [33]: article = Article.objects.get(pk=1)

In [34]: article.title
Out[34]: 'first'

In [35]: article.title = 'first-update'

In [36]: article.save()

In [37]: article.title
Out[37]: 'first-update'
```



### Delete

```python
In [38]: article = Article.objects.get(pk=1)

In [39]: article.delete()
Out[39]: (1, {'articles.Article': 1})

# 조회하면 존재하지 않는다고 나옴
In [40]: Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```

![image-20220418032656816](0308%20Model.assets/image-20220418032656816.png)



<hr>

## 게시판 만들기

### 1. Create

#### Index - 목록

- pages/views

  ```python
  from django.shortcuts import render
  from .models import Article
  
  # Create your views here.
  def index(request):
      # 모든 게시글을 출력
      articles = Article.objects.all()
      context = {
          'articles' : articles
      }
      return render(request, 'pages/index.html', context)
  
  ```

  ```python
  # 정렬 순서를 내림차순으로 방법
  def index(request):
      # 파이썬이용: DB로 부터 받은 쿼리셋을 파이썬 언어로 변경
      article = Article.object.all()[::-1]
      # DB조작: 처음부터 내림차순 쿼리셋으로 받음
      article = Article.object.order_by('-pk')
  ```

  

- index.html

  ```html
  {% extends 'base.html' %}
  {% block body %}
    <h1>안녕하세요</h1>
  
    {% for article in articles %}
      <p> {{ article.title }} </p>
      <hr>
    {% endfor %}
  {% endblock body %}
  
  ```

  

#### Create - New

>  form을 이용하여 new에서 내용을 던져 create에서 받기

- url

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('', views.index, name='index'),
      path('new', views.new, name='new'),
      path('create/', views.create, name="create" ),
  ]
  
  ```

  

- views

  ```python
  def new(request):
      return render(request, 'pages/new.html')
  
  def create(request):
      # 사용자의 입력을 받아서
      title = request.GET.get('title')
      content = request.GET.get('content')
      #  DB에 저장
      article = Article()
      article.title = title
      article.content = content
      article.save()
      # template에서 보여져야해
      context ={
          'article' : article
      }
      return render(request, 'pages/create.html', context)
  ```

  

- template

  - new.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1> NEW </h1>
    <form action="{% url 'pages:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">제목: </label>
      <input type='text' id='title' name='title'>
      <label for="content">내용: </label>
      <textarea id="content" name="content"></textarea>
  
      <input type='submit' value="제출">
    </form>
  {% endblock body %}
  ```

  - create.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>{{ article.id }}번째 글이 작성 완료되었습니다.</h1>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
  {% endblock body %}
  ```

  

- 흐름 사진

- <img src="0308%20Model.assets/image-20220308162356062.png" alt="image-20220308162356062" style="zoom:50%;" />

  <img src="0308%20Model.assets/image-20220308162119229.png" alt="image-20220308162119229" style="zoom:50%;" />



- 출력 결과

<img src="0308%20Model.assets/image-20220308162257458.png" alt="image-20220308162257458" style="zoom:50%;" />

<img src="0308%20Model.assets/image-20220308162416544.png" alt="image-20220308162416544" style="zoom:50%;" />

<img src="0308%20Model.assets/image-20220308162431912.png" alt="image-20220308162431912" style="zoom:50%;" />

### 2. READ 

#### Index - 목록 링크

>  Variable roution (변수화) => 게시글마다 각자 다른 url을 써서 다른 링크로 들어갈 수 있도록!

- index.html

  ```html
  {% extends 'base.html' %}
  {% block body %}
    <h1>안녕하세요</h1>
  
    {% for article in articles %}
      <a href="{% url 'pages:detail' article.pk %}">
        <p> {{ article.title }} </p> 
      </a>
      <hr>
    {% endfor %}
  {% endblock body %}
  ```



#### Detail - variable routing

- urls.py

  > variable routing

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/', views.detail, name='detail')
  ]
  ```

  

- views.py 

  > 개별 게시글 상세 페이지, 글의 번호(pk)를 활용하여 페이지 구현 
  >
  > => Variable Routing 이용!!
  >
  > article이라는 db에서 pk를 get 해서 가져와서 url에 쓸거임

  ```python
  def detail(request, pk):
      article = Article.objects.get(pk=pk)
      context ={
          'article' : article
      }
      return render(request, 'pages/detail.html', context)
  ```

  

- detail.html (template)

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>{{article.pk}}번 글</h1>
    <h2>{{article.title}}</h2>
    <p>{{article.created_at}}</p>
    <hr>
    <p>{{article.content}}</p>
  {% endblock body %}
  
  ```




### 3.Delete

- urls

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/delete/', views.delete, name='delete')
  ]
  ```

- views

  ```python
  def delete(request, pk):
      article = Article.objects.get(pk=pk)
      article.delete()
      return redirect('pages:index')
  ```

  

### 4. Edit - Update

- urls.py

  ```python
  from django.urls import path
  from . import views
  
  app_name='pages'
  urlpatterns = [
      path('<int:pk>/edit/', views.edit, name='edit'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```

  

- views.py

  ```python
  def edit(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article' : article
      }
      return render(request, 'pages/edit.html', context)
  ```

  ```python
  def update(request, pk):
      title = request.GET.get('title')
      content = request.GET.get('content')
  
      article = Article.objects.get(pk=pk)
      article.title = title
      article.content = content
      article.save()
      return redirect('pages:detail', article.pk)
  ```

  - **에러**

    ![image-20220309010837967](0308%20Model.assets/image-20220309010837967.png)

    - 에러이유

      ```python
      article = Article().objects.get(pk=pk)
      ```

      Article() 은 인스턴스이고, Article은 클래스이다.

      인스턴스는 관리자에 액세스할 수 없고, 우리는 Article 클래스에 있는 객체를 pk에 맞는 정보를 article에 저장해야 한다.

    - **에러수정** 

    ```python
    article = Article.objects.get(pk=pk)
    ```

    

  

- edit.html

  ```html
  {% extends 'base.html' %}
  
  {% block body %}
    <h1>Edit</h1>
    <form action="{% url 'pages:update' article.pk %}" method="POST">
      {% csrf_token %}
      <lable for="title">제목: </label>
      <input type=text id='title' name='title' value='{{article.title}}'>
      <label for='content'>내용: </label>
      <textarea id='content' name='content'>{{article.content}}</textarea>
  
      <input type='submit' value='제출'>
    </form>
  {% endblock body %}
  
  
  ```
  
  

## Redirect

> 다시 다른 웹페이지로 돌아가도록 지시

- 새 URL로 요청을 다시 보냄
- 인자에 따라 HttpResponseRedirect를 반환
- 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성

![image-20220309012420931](0308%20Model.assets/image-20220309012420931.png)

```python
return redirect('articles:detail', article.pk) # **kwargs

#=> 동등한 표현 
return redirect('articles:detail', pk = article.pk) #*args
return redirect(f'/articles/{article.pk}/')
```

- 함수의 인자를 변수화된 URL로 받아야하기 때문에 `'articles:detail'` 이런식으로 받는 형식을 따름.

- 근데 `return redirect(f'/articles/{article.pk}/')`로 받으면 변수가 아니고 상수가 되므로 나중에 변경되면 응답을 못해 

- `return render(request, 'articles/detail.html', context)` 로 쓰면 안되나요?
  - views를 거치지 않기 때문에 에러가 뜬다.

<img src="0308%20Model.assets/image-20220308231225527.png" alt="image-20220308231225527" style="zoom:50%;" />

***상태코드 302*** : **하이퍼텍스트 전송 프로토콜 (HTTP)의 302 Found 리다이렉트 상태 응답 코드는 클라이언트가 요청한 리소스가 Location 헤더에 주어진 URL에 일시적으로 이동되었음을 가리킨다.**



## HTTP method 

> form 형식 속 method="GET->POST"

| GET                                     | POST                                              |
| --------------------------------------- | ------------------------------------------------- |
| 특정 리소스를 가져오도록 요청할 때 사용 | 서버로 데이터를 전송할 때 사용                    |
| 반드시 데이터를 가져올 때만 사용        | 리소스를 생성/변경하기 위해 HTTP body에 담아 전송 |
| DB에 변화를 주지 않음                   | 서버에 변경사항을 만듬                            |
| CRUD 중 R                               | CRUD 중 CUD                                       |



- 사이트 간 요청 위조 <403 forbidden>

![image-20220308174615359](0308%20Model.assets/image-20220308174615359.png)

> 보통 POST를 쓴다.

<CSRF 사이트 간 요청 위조로 인해 금지되어있다>

get : 정보 조회로 데이터를 가져오기만 하기때문에 body가 아닌 쿼리파라미터로 전송한다. => URL에 노출이 된다

post : 서버로 데이터를 전송할 때 사용하기 때문에 HTTP body에 담아 전송한다( id, password ) => URL에 숨겨서 볼 수 있도록

![image-20220308175010629](0308%20Model.assets/image-20220308175010629.png)

- **{% csrf_token %}**

 		:	 input 태그!!! type=hidden으로 되어있다. 서버에 요청해서 허가해달라는 뜻임



# 총정리

1. Model : 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
2. Database : 체계화된 데이터의 집합
3. Migration : Django가 model에 생긴 변화를 반영하는 방법

4. ORM : 객체 지향 프로그래밍(OOP) 과 RDBMS 의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

5. Database API : DB를 조작하기 위한 도구 (QuerySet API, CRUD)

   